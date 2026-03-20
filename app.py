from model.fact_checker import fact_check
from utils.translator import translate_text

print("=== AI Fact Checker ===")

news = input("Enter news text: ")

translated = translate_text(news)
verdict, score = fact_check(translated)

print("\nTranslated:", translated)
print("Verdict:", verdict)
print("Confidence:", score)
