def analyze_credit_score(credit_score):
    if credit_score >= 750:
        return "Congratulations! Your credit score is excellent. You're eligible for the best interest rates and financial products."
    elif 700 <= credit_score < 750:
        return "Great job! Your credit score is good. You have access to competitive interest rates and a variety of financial options."
    elif 650 <= credit_score < 700:
        return "Your credit score is fair. While you may qualify for loans, interest rates may be higher. Consider improving your score for better terms."
    elif 600 <= credit_score < 650:
        return "Your credit score needs improvement. You may face challenges in obtaining credit, and interest rates may be less favorable."
    else:
        return "Your credit score is poor. It's essential to work on improving it to access better financial opportunities and lower interest rates."
    

def main():
    try:
        credit_score = int(input("Please enter your credit score: "))
        if 300 <= credit_score <= 850:
            result = analyze_credit_score(credit_score)
            print(result)
        else:
            print("Invalid credit score. Please enter a score between 300 and 850.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for your credit score.")


if __name__ == "__main__":
    main()