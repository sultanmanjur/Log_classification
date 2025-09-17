from sentence_transformers import SentenceTransformer
import joblib
import os

model = SentenceTransformer('all-MiniLM-L6-v2')
clf_path = os.path.join('models', 'logg_classifier.joblib')
clf = joblib.load(clf_path)

def classify_with_bert(log_message):
    embedding = model.encode([log_message])
    predicted_proba = clf.predict_proba(embedding)[0]
    
    if predicted_proba.max() < 0.4:
        return "Unclassified"
    predicted_label = clf.predict(embedding)[0]
    return predicted_label

if __name__ == "__main__":
    #print("Script started")
    test_logs = [
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active.",
        "Invoice generation process aborted for order ID 8910 due to invalid tax calculation module.",
        "The 'BulkEmailSender' feature is no longer supported. Use 'EmailCampaignManager' for improved functionality.",
        "Hey bro, chill out",
        "ThirdPartyAPI,Suspicious login activity detected from 192.168.24.250"
    ]
    try:
        for log in test_logs:
            classification = classify_with_bert(log)
            print(f"Log: '{log}' => Classification: '{classification}'")
    except Exception as e:
        print(f"Error: {e}")