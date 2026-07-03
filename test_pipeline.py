from backend.pipeline import analyze_repository

report = analyze_repository(

    "https://github.com/WebGoat/WebGoat"

)

print(report)