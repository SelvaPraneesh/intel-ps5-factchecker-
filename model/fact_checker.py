from transformers import pipeline

classifier = pipeline("text-classification")

def fact_check(text):
    result = classifier(text)
    
    score = result[0]['score']
    
    if score > 0.7:
        verdict = "Likely Real"
    else:
        verdict = "Possibly Fake"
    
    return verdict, score
