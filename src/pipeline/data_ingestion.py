import json
import re

class DataIngestion:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path
        self.cleaned_data = []

    def load_data(self):
        with open(self.json_file_path, 'r') as f:
            self.raw_data = json.load(f)

    def preprocess_data(self):
        for doc in self.raw_data:
            content_cleaned = re.sub(r'\s+', ' ', doc["content"]).strip()
            key_metrics = self.extract_numerical_data(content_cleaned)
            cleaned_doc = {
                "document_id": doc["document_id"],
                "title": doc["title"],
                "company": doc["company"],
                "date": doc["date"],
                "topics": doc["topics"],
                "content": content_cleaned,
                "key_metrics": key_metrics
            }
            self.cleaned_data.append(cleaned_doc)

    def extract_numerical_data(self, content):
        metrics = {
            "revenue": self.extract_value(r'Revenue: \$([0-9,.]+)', content),
            "net_profit": self.extract_value(r'Net Profit: \$([0-9,.]+)', content),
            "revenue_growth_rate": self.extract_value(r'Revenue Growth Rate: ([0-9,.]+)%', content),
            "operational_cost_reduction": self.extract_value(r'Operational Cost Reduction: ([0-9,.]+)%', content)
        }
        return metrics

    def extract_value(self, pattern, text):
        match = re.search(pattern, text)
        return float(match.group(1).replace(',', '')) if match else None

    def get_data(self):
        return self.cleaned_data