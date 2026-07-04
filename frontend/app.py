import streamlit as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from backend.pipeline import analyze_repository

st.set_page_config(
    page_title="AI Repository Explorer",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Repository Explorer")

st.markdown("""
Analyze GitHub repositories using AI-assisted security analysis.

Features:
- Repository Intelligence
- Semgrep Security Scan
- AI Representative Snippet Selection
- OWASP & CWE Mapping
- Business Impact Analysis
""")

repo = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/user/repository"
)

if st.button("Analyze Repository"):

    if not repo:
        st.warning("Enter a repository URL.")
        st.stop()

    with st.spinner("Analyzing..."):

        report = analyze_repository(repo)

    st.success("Analysis Completed!")

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Files", report["total_files"])
    c2.metric("Findings", report["total_findings"])
    c3.metric("Unique Vulnerabilities", report["unique_vulnerabilities"])
    c4.metric(
        "Primary Language",
        report["languages"]["primary_language"]
    )
    c5 = st.columns(5)[4]

    c5.metric(
     "Risk Score",
     report["risk_score"]
    )
    st.divider()

    st.header("Repository Intelligence")
    summary = report["repository_summary"]

    if summary:

     st.subheader("Repository Type")
     st.info(summary.get("repository_type","Unknown"))

     st.subheader("Architecture")
     st.info(summary.get("architecture","Unknown"))

     st.subheader("Interesting Files")

     for file in summary.get("security_sensitive_files",[]):

        st.write("📄",file)

     st.subheader("Security Sensitive Components")

     for component in summary.get(
        "security_sensitive_components",
        []
     ):

        st.write("🛡",component)

     st.subheader("AI Summary")

     st.success(summary.get("summary",""))
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Languages")
        st.json(report["languages"])

    with col2:
        st.subheader("Frameworks")
        st.write(report["frameworks"])

    st.divider()

    st.header("Security Findings")

    for finding in report["results"]:

        with st.expander(
            f"{finding['label']} | {finding['title']}",
            expanded=False
        ):

            left, right = st.columns(2)

            with left:

                st.markdown(f"### 🏷 Label")
                st.info(finding["label"])

                st.markdown("### Severity")
                st.error(finding["severity"])

                st.markdown("### Risk")
                st.warning(finding["risk"])

                st.markdown("### Confidence")
                st.success(finding["confidence"])

            with right:

                st.markdown("### OWASP")
                st.info(finding["owasp"])

                st.markdown("### CWE")
                st.info(finding["cwe"])

                st.markdown("### Occurrences")
                st.metric("", finding["occurrences"])

            st.divider()

            st.subheader("Summary")
            st.write(finding["summary"])

            st.subheader("Business Impact")
            st.write(finding["impact"])

            st.subheader("Recommendation")
            st.success(finding["recommendation"])

            st.subheader("Execution Flow")

            st.write(
             finding["flow"]["flow"]
             )

            st.subheader("Root Cause")

            st.warning(
              finding["flow"]["root_cause"]
            )

            st.subheader("Possible Attack")

            st.error(
             finding["flow"]["attack"]
            )

            st.subheader("Suggested Fix")

            st.success(
             finding["flow"]["fix"]
            )

            st.subheader("Why AI Selected This Snippet")
            st.write(finding["reason"])

            st.subheader("Affected File")
            st.subheader("Function")

            st.code(
             finding["function"]["name"]
            )
            st.write("Function Lines")

            st.code(
                f"{finding['function']['start_line']} - {finding['function']['end_line']}"
            )
            st.code(
                finding["snippet"]["file"]
            )

            st.subheader("Lines")

            st.code(
                f"{finding['snippet']['start_line']} - {finding['snippet']['end_line']}"
            )

            st.subheader("Representative Code")

            st.code(
                finding["snippet"]["code"],
                language="python"
            )