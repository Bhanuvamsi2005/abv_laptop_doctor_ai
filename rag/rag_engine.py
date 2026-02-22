# #
# # from rag.retriever import retrieve_documents
# #
# # def generate_solution(company, model, user_problem, structured_issue):
# #     issue_text = structured_issue["normalized"]
# #
# #     docs = retrieve_documents(issue_text)
# #
# #     if not docs:
# #         return "Sorry, I couldn't find a confident match. Please describe the issue more clearly."
# #
# #     return build_response(docs)
# #
# #
# # def build_response(docs):
# #     best_match = docs[0]
# #
# #     response = "Suggested Fix:\n"
# #
# #     for i, sol in enumerate(best_match["solutions"], start=1):
# #         response += f"{i}. {sol}\n"
# #
# #     return response
#
#
#
#
#
#


# from rag.retriever import retrieve_documents
#
# FOLLOW_UP_SIGNALS = [
#     "still not working",
#     "not working",
#     "same issue",
#     "problem persists"
# ]
#
#
# def is_follow_up(user_text):
#     user_text = user_text.lower()
#     return any(signal in user_text for signal in FOLLOW_UP_SIGNALS)
#
#
# def format_severity(severity):
#     if severity == "critical":
#         return "🔴 Critical"
#
#     if severity == "warning":
#         return "🟠 Warning"
#
#     return "🟢 Minor"
#
#
# def generate_solution(company, model, user_problem, structured_issue, last_issue=None):
#     issue_text = structured_issue["normalized"]
#
#     if is_follow_up(issue_text) and last_issue:
#         return handle_follow_up(last_issue)
#
#     docs = retrieve_documents(issue_text)
#
#     if not docs:
#         return (
#             "⚠ No confident match found.\n"
#             "Please describe the issue more clearly."
#         ), last_issue
#
#     best_match = docs[0]
#
#     severity = format_severity(best_match["severity"])
#
#     response = build_response(best_match, severity)
#
#     return response, best_match["issue"]
#
#
# def handle_follow_up(last_issue):
#     response = (
#         f"I see the issue is still unresolved ({last_issue}).\n\n"
#         "Advanced Suggestions:\n"
#         "1. Restart the device if not already done.\n"
#         "2. Run full hardware diagnostics.\n"
#         "3. Check for driver conflicts.\n"
#         "4. Escalate to IT support if needed."
#     )
#
#     return response, last_issue
#
#
# def build_response(doc, severity):
#     response = f"{severity}\n\nSuggested Fix:\n"
#
#     for i, sol in enumerate(doc["solutions"], start=1):
#         response += f"{i}. {sol}\n"
#
#     return response
#
#


# from rag.retriever import retrieve_documents
# from gemini_helper import ask_gemini
#
# FOLLOW_UP_SIGNALS = [
#     "still not solved",
#     "still not working",
#     "not solved",
#     "problem persists"
# ]
#
#
# def is_follow_up(user_text):
#     user_text = user_text.lower()
#     return any(signal in user_text for signal in FOLLOW_UP_SIGNALS)
#
#
# def format_severity(severity):
#     if severity == "critical":
#         return "🔴 Critical"
#
#     if severity == "warning":
#         return "🟠 Warning"
#
#     return "🟢 Minor"
#
#
# def generate_solution(company, model, user_problem, structured_issue, last_issue=None):
#     issue_text = structured_issue["normalized"]
#
#     if is_follow_up(issue_text) and last_issue:
#         return advanced_troubleshooting(last_issue)
#
#     docs = retrieve_documents(issue_text)
#
#     # ✅ FALLBACK TO GEMINI 🚀
#     if not docs:
#         gemini_response = ask_gemini(user_problem)
#
#         response = (
#             "🤖 AI Assistance (Gemini Fallback)\n\n"
#             + gemini_response
#         )
#
#         return response, last_issue
#
#     best_match = docs[0]
#
#     severity = format_severity(best_match["severity"])
#
#     response = build_basic_response(best_match, severity)
#
#     return response, best_match["issue"]
#
#
# def build_basic_response(doc, severity):
#     response = f"{severity}\n\nSuggested Fix:\n"
#
#     for i, sol in enumerate(doc["solutions"], start=1):
#         response += f"{i}. {sol}\n"
#
#     return response
#
#
# def advanced_troubleshooting(issue):
#     response = (
#         f"I understand the issue is still unresolved ({issue}).\n\n"
#         "Advanced Troubleshooting Steps:\n"
#         "1. Run full hardware diagnostics\n"
#         "2. Reinstall drivers\n"
#         "3. Check OS conflicts\n"
#         "4. Contact IT support if needed"
#     )
#
#     return response, issue
#
# from rag.retriever import retrieve_documents
# from gemini_helper import ask_gemini
#
# FOLLOW_UP_SIGNALS = [
#     "still not solved",
#     "still not working",
#     "not solved",
#     "problem persists"
# ]
#
#
# def is_follow_up(user_text):
#     user_text = user_text.lower()
#     return any(signal in user_text for signal in FOLLOW_UP_SIGNALS)
#
#
# def format_severity(severity):
#     if severity == "critical":
#         return "🔴 Critical"
#
#     if severity == "warning":
#         return "🟠 Warning"
#
#     return "🟢 Minor"
#
#
# def format_confidence(score):
#     percentage = int(score * 100)
#     return f"(Confidence: {percentage}%)"
#
#
# def generate_solution(company, model, user_problem, structured_issue, last_issue=None):
#     issue_text = structured_issue["normalized"]
#
#     if is_follow_up(issue_text) and last_issue:
#         return advanced_troubleshooting(last_issue)
#
#     doc, score = retrieve_documents(issue_text)
#
#     # ✅ FALLBACK TO GEMINI
#     if not doc:
#         gemini_response = ask_gemini(user_problem)
#
#         response = (
#             "🤖 AI Assistance (Gemini Fallback)\n"
#             f"{format_confidence(score)}\n\n"
#             + gemini_response
#         )
#
#         return response, last_issue
#
#     severity = format_severity(doc["severity"])
#
#     response = build_basic_response(doc, severity, score)
#
#     return response, doc["issue"]
#
#
# def build_basic_response(doc, severity, score):
#     response = f"{severity} {format_confidence(score)}\n\nSuggested Fix:\n"
#
#     for i, sol in enumerate(doc["solutions"], start=1):
#         response += f"{i}. {sol}\n"
#
#     return response
#
#
# def advanced_troubleshooting(issue):
#     response = (
#         f"I understand the issue is still unresolved ({issue}).\n\n"
#         "Advanced Troubleshooting Steps:\n"
#         "1. Run full hardware diagnostics\n"
#         "2. Reinstall drivers\n"
#         "3. Check OS conflicts\n"
#         "4. Contact IT support if needed"
#     )
#
#     return response, issue










#
# from rag.retriever import retrieve_documents
# from gemini_helper import ask_gemini
#
#
# FOLLOW_UP_SIGNALS = [
#     "still not solved",
#     "still not working",
#     "not solved",
#     "problem persists",
#     "issue not fixed",
#     "same problem"
# ]
#
#
# def is_follow_up(user_text):
#     user_text = user_text.lower()
#     return any(signal in user_text for signal in FOLLOW_UP_SIGNALS)
#
#
# def format_severity(severity):
#
#     if severity == "critical":
#         return "🔴 Critical"
#
#     if severity == "warning":
#         return "🟠 Warning"
#
#     return "🟢 Minor"
#
#
# def format_confidence(score):
#
#     if score is None:
#         return ""
#
#     percentage = int(score * 100)
#     return f"(Confidence: {percentage}%)"
#
#
# def generate_solution(company, model, user_problem, structured_issue, last_issue=None):
#
#     issue_text = structured_issue["normalized"]
#
#     # ✅ FOLLOW-UP HANDLING
#     if is_follow_up(issue_text) and last_issue:
#         return advanced_troubleshooting(last_issue)
#
#     doc, score = retrieve_documents(issue_text)
#
#     # ✅ NO MATCH → GEMINI FALLBACK
#     if not doc:
#
#         gemini_response = ask_gemini(user_problem)
#
#         # ✅ Gemini Failure / Quota Safe
#         if gemini_response.startswith("⚠"):
#
#             response = (
#                 "⚠ No confident match found.\n"
#                 "Using fallback troubleshooting.\n\n"
#                 "Suggested Fix:\n"
#                 "1. Restart the device\n"
#                 "2. Update drivers\n"
#                 "3. Run hardware diagnostics\n"
#                 "4. Check system updates\n"
#             )
#
#             return response, last_issue
#
#         response = (
#             "🤖 AI Assistance (Gemini Fallback)\n"
#             f"{format_confidence(score)}\n\n"
#             + gemini_response
#         )
#
#         return response, last_issue
#
#     severity = format_severity(doc["severity"])
#
#     response = build_basic_response(doc, severity, score)
#
#     return response, doc["issue"]
#
#
# def build_basic_response(doc, severity, score):
#
#     response = f"{severity} {format_confidence(score)}\n\nSuggested Fix:\n"
#
#     for i, sol in enumerate(doc["solutions"], start=1):
#         response += f"{i}. {sol}\n"
#
#     return response
#
#
# def advanced_troubleshooting(issue):
#
#     response = (
#         f"I understand the issue is still unresolved ({issue}).\n\n"
#         "Advanced Troubleshooting Steps:\n"
#         "1. Run full hardware diagnostics\n"
#         "2. Reinstall device drivers\n"
#         "3. Check OS conflicts\n"
#         "4. Scan for hardware failures\n"
#         "5. Contact IT support if needed"
#     )
#
#     return response, issue
#




# from rag.retriever import retrieve_documents
# from gemini_helper import ask_gemini
#
# FOLLOW_UP_SIGNALS = [
#     "still not solved",
#     "still not working",
#     "not solved",
#     "problem persists",
#     "issue not fixed",
#     "same problem"
# ]
#
#
# def is_follow_up(user_text):
#     user_text = user_text.lower()
#     return any(signal in user_text for signal in FOLLOW_UP_SIGNALS)
#
#
# def format_severity(severity):
#     if severity == "critical":
#         return "🔴 Critical"
#     if severity == "warning":
#         return "🟠 Warning"
#     return "🟢 Minor"
#
#
# def format_confidence(score):
#     if score is None:
#         return ""
#     percentage = int(score * 100)
#     return f"(Confidence: {percentage}%)"
#
#
# def generate_solution(company, model, user_problem, structured_issue, last_issue=None):
#     issue_text = structured_issue["normalized"]
#
#     # ✅ FOLLOW-UP HANDLING
#     if is_follow_up(issue_text) and last_issue:
#         return advanced_troubleshooting(last_issue)
#
#     doc, score = retrieve_documents(issue_text)
#
#     # ✅ NO MATCH → GEMINI FALLBACK
#     if not doc:
#         gemini_response = ask_gemini(user_problem)
#
#         # ✅ Check for quota/failure
#         if gemini_response.startswith("⚠ QUOTA_EXCEEDED"):
#             response = (
#                 "⚠ Gemini API quota exceeded.\n"
#                 "Using local troubleshooting.\n\n"
#                 "Suggested Fix:\n"
#                 "1. Restart the device\n"
#                 "2. Update drivers\n"
#                 "3. Run hardware diagnostics\n"
#                 "4. Check system updates\n"
#             )
#             return response, last_issue
#
#         if gemini_response.startswith("⚠ GEMINI_FAILURE"):
#             response = (
#                 "⚠ AI service temporarily unavailable.\n"
#                 "Using local troubleshooting.\n\n"
#                 "Suggested Fix:\n"
#                 "1. Restart the device\n"
#                 "2. Update drivers\n"
#                 "3. Run hardware diagnostics\n"
#                 "4. Check system updates\n"
#             )
#             return response, last_issue
#
#         # ✅ Successful Gemini response
#         response = (
#             "🤖 AI Assistance (Gemini)\n\n"
#             + gemini_response
#         )
#         return response, last_issue
#
#     # ✅ KB MATCH FOUND
#     severity = format_severity(doc["severity"])
#     response = build_basic_response(doc, severity, score)
#     return response, doc["issue"]
#
#
# def build_basic_response(doc, severity, score):
#     response = f"{severity} {format_confidence(score)}\n\nSuggested Fix:\n"
#     for i, sol in enumerate(doc["solutions"], start=1):
#         response += f"{i}. {sol}\n"
#     return response
#
#
# def advanced_troubleshooting(issue):
#     response = (
#         f"I understand the issue is still unresolved ({issue}).\n\n"
#         "Advanced Troubleshooting Steps:\n"
#         "1. Run full hardware diagnostics\n"
#         "2. Reinstall device drivers\n"
#         "3. Check OS conflicts\n"
#         "4. Scan for hardware failures\n"
#         "5. Contact IT support if needed"
#     )
#     return response, issue











from rag.retriever import retrieve_documents
from gemini_helper import ask_gemini

FOLLOW_UP_SIGNALS = [
    "still not solved",
    "still not working",
    "not solved",
    "problem persists",
    "issue not fixed",
    "same problem"
]


def is_follow_up(user_text):
    user_text = user_text.lower()
    return any(signal in user_text for signal in FOLLOW_UP_SIGNALS)


def format_severity(severity):
    if severity == "critical":
        return "🔴 Critical"
    if severity == "warning":
        return "🟠 Warning"
    return "🟢 Minor"


def format_confidence(score):
    if score is None:
        return ""
    percentage = int(score * 100)
    return f"(Confidence: {percentage}%)"


def generate_solution(company, model, user_problem, structured_issue, last_issue=None):
    """
    Main function to generate solutions using either KB or Gemini fallback
    """
    issue_text = structured_issue["normalized"]

    # ✅ FOLLOW-UP HANDLING
    if is_follow_up(issue_text) and last_issue:
        return advanced_troubleshooting(last_issue)

    # Try to get solution from knowledge base
    doc, score = retrieve_documents(issue_text)

    # ✅ NO MATCH IN KB → TRY GEMINI
    if not doc:
        gemini_response = ask_gemini(user_problem)

        # Handle different Gemini response types
        if gemini_response == "⚠ QUOTA_EXCEEDED":
            response = (
                "📊 **Gemini API Daily Limit Reached**\n\n"
                "The free tier allows 20 requests per day. You've used your quota for today.\n\n"
                "**Using Local Knowledge Base:**\n"
                "1. Restart your device\n"
                "2. Check for driver updates\n"
                "3. Run Windows/Mac diagnostics\n"
                "4. Check hardware connections\n\n"
                "The quota will reset in 24 hours, or you can:\n"
                "• Use a different API key\n"
                "• Set up billing for higher limits"
            )
            return response, last_issue

        elif gemini_response == "⚠ GEMINI_INVALID_API_KEY":
            response = (
                "⚠ **Invalid Gemini API Key**\n\n"
                "The API key in your .env file is invalid. Please check:\n"
                "1. Go to https://makersuite.google.com/app/apikey\n"
                "2. Create a new API key\n"
                "3. Update your .env file\n\n"
                "**Using Local Troubleshooting:**\n"
                "1. Restart your device\n"
                "2. Update drivers\n"
                "3. Run hardware diagnostics"
            )
            return response, last_issue

        elif gemini_response == "⚠ GEMINI_FAILURE" or gemini_response == "⚠ GEMINI_NOT_CONFIGURED":
            response = (
                "⚠ **AI Service Temporarily Unavailable**\n\n"
                "**Using Local Troubleshooting:**\n"
                "1. Restart your device\n"
                "2. Update system drivers\n"
                "3. Run built-in diagnostics\n"
                "4. Check hardware connections\n"
                "5. Scan for malware\n\n"
                "Please try again in a few minutes."
            )
            return response, last_issue

        elif gemini_response.startswith("⚠"):
            # Generic Gemini error
            response = (
                "⚠ **AI Assistance Unavailable**\n\n"
                "**Basic Troubleshooting Steps:**\n"
                "1. Restart your laptop\n"
                "2. Check for Windows/macOS updates\n"
                "3. Update device drivers\n"
                "4. Run hardware diagnostic tools\n"
                "5. Check for overheating or physical damage\n\n"
                f"Error: {gemini_response}"
            )
            return response, last_issue

        else:
            # ✅ Successful Gemini response
            response = (
                "🤖 **AI Assistance (Gemini)**\n\n"
                f"{gemini_response}\n\n"
                "---\n"
                "*Need more help? Feel free to ask follow-up questions.*"
            )
            return response, last_issue

    # ✅ KB MATCH FOUND
    severity = format_severity(doc["severity"])
    response = build_kb_response(doc, severity, score)
    return response, doc["issue"]


def build_kb_response(doc, severity, score):
    """
    Build response from knowledge base match
    """
    response = f"{severity} {format_confidence(score)}\n\n"
    response += "**Suggested Fix:**\n"

    for i, sol in enumerate(doc["solutions"], start=1):
        # Format solutions nicely
        if isinstance(sol, str):
            response += f"{i}. {sol}\n"
        else:
            response += f"{i}. {str(sol)}\n"

    # Add helpful footer
    response += "\n---\n"
    response += "*If this doesn't solve your issue, try describing the problem in more detail.*"

    return response


def advanced_troubleshooting(issue):
    """
    Handle follow-up queries when previous solutions didn't work
    """
    response = (
        f"I understand the issue is still unresolved: **{issue}**\n\n"
        "**Advanced Troubleshooting Steps:**\n\n"
        "1. **Run Full Hardware Diagnostics**\n"
        "   • Use built-in diagnostics (Dell SupportAssist, HP PC Hardware Diagnostics, Apple Diagnostics)\n"
        "   • Check for hardware failure codes\n\n"
        "2. **Reinstall/Update Device Drivers**\n"
        "   • Boot into Safe Mode\n"
        "   • Uninstall and reinstall affected drivers\n"
        "   • Download latest drivers from manufacturer website\n\n"
        "3. **Check OS-Level Conflicts**\n"
        "   • Review recent updates/installations\n"
        "   • Perform System Restore (Windows) or Time Machine (Mac)\n"
        "   • Check Event Viewer (Windows) or Console (Mac) for errors\n\n"
        "4. **Test in Safe Mode**\n"
        "   • If issue disappears in Safe Mode, it's likely software/driver related\n"
        "   • If issue persists, it's likely hardware related\n\n"
        "5. **Hardware Checks**\n"
        "   • Check for loose connections\n"
        "   • Test with minimal hardware configuration\n"
        "   • Listen for unusual sounds (fans, hard drives)\n\n"
        "6. **Escalate to Professional Support**\n"
        "   • Contact manufacturer support\n"
        "   • Visit authorized service center\n"
        "   • Provide them with error codes and troubleshooting steps already attempted\n\n"
        "---\n"
        "*Need specific guidance on any of these steps? Let me know!*"
    )
    return response, issue


def build_basic_response(doc, severity, score):
    """
    Legacy function - kept for compatibility
    """
    return build_kb_response(doc, severity, score)








# from rag.retriever import retrieve_documents
# from gemini_helper import ask_gemini
#
# FOLLOW_UP_SIGNALS = [
#     "still not solved",
#     "still not working",
#     "not solved",
#     "problem persists",
#     "issue not fixed",
#     "same problem"
# ]
#
#
# def is_follow_up(user_text):
#     user_text = user_text.lower()
#     return any(signal in user_text for signal in FOLLOW_UP_SIGNALS)
#
#
# def format_severity(severity):
#
#     if severity == "critical":
#         return "🔴 Critical"
#
#     if severity == "warning":
#         return "🟠 Warning"
#
#     return "🟢 Minor"
#
#
# def format_confidence(score):
#
#     if score is None:
#         return ""
#
#     percentage = int(score * 100)
#     return f"(Confidence: {percentage}%)"
#
#
# def generate_solution(company, model, user_problem, structured_issue, last_issue=None):
#
#     issue_text = structured_issue["normalized"]
#
#     # ✅ FOLLOW-UP DETECTION
#     if is_follow_up(issue_text) and last_issue:
#         return advanced_troubleshooting(last_issue)
#
#     doc, score = retrieve_documents(issue_text)
#
#     # ✅ NO MATCH → GEMINI FALLBACK
#     if not doc:
#
#         gemini_response = ask_gemini(user_problem)
#
#         # ✅ QUOTA / FAILURE SAFE HANDLING
#         if gemini_response.startswith("⚠"):
#
#             response = (
#                 "⚠ No confident match found.\n"
#                 "Using local diagnostic intelligence.\n\n"
#                 "Suggested Fix:\n"
#                 "1. Restart the device\n"
#                 "2. Update system drivers\n"
#                 "3. Run built-in diagnostics\n"
#                 "4. Check hardware connections\n"
#             )
#
#             return response, last_issue
#
#         # ✅ GEMINI SUCCESS RESPONSE
#         response = (
#             "🤖 AI Assistance (Gemini Fallback)\n"
#             f"{format_confidence(score)}\n\n"
#             + gemini_response
#         )
#
#         return response, last_issue
#
#     # ✅ KB MATCH FOUND
#     severity = format_severity(doc["severity"])
#
#     response = build_basic_response(doc, severity, score)
#
#     return response, doc["issue"]
#
#
# def build_basic_response(doc, severity, score):
#
#     response = f"{severity} {format_confidence(score)}\n\nSuggested Fix:\n"
#
#     for i, sol in enumerate(doc["solutions"], start=1):
#         response += f"{i}. {sol}\n"
#
#     return response
#
#
# def advanced_troubleshooting(issue):
#
#     response = (
#         f"I understand the issue is still unresolved ({issue}).\n\n"
#         "Advanced Troubleshooting Steps:\n"
#         "1. Run full hardware diagnostics\n"
#         "2. Reinstall related drivers\n"
#         "3. Check OS-level conflicts\n"
#         "4. Test in Safe Mode\n"
#         "5. Verify recent updates / changes\n"
#         "6. Escalate to IT / hardware support if needed"
#     )
#
#     return response, issue



# from rag.retriever import retrieve_documents
# from gemini_helper import ask_gemini
#
# FOLLOW_UP_SIGNALS = [
#     "still not solved",
#     "still not working",
#     "not solved",
#     "problem persists",
#     "same problem",
#     "issue not fixed"
# ]
#
#
# def is_follow_up(user_text):
#     user_text = user_text.lower()
#     return any(signal in user_text for signal in FOLLOW_UP_SIGNALS)
#
#
# def format_severity(severity):
#     if severity == "critical":
#         return "🔴 Critical"
#
#     if severity == "warning":
#         return "🟠 Warning"
#
#     return "🟢 Minor"
#
#
# def format_confidence(score):
#     if score is None:
#         return ""
#
#     percentage = int(score * 100)
#     return f"(Confidence: {percentage}%)"
#
#
# def generate_solution(company, model, user_problem, structured_issue, last_issue=None):
#
#     issue_text = structured_issue["normalized"]
#
#     if is_follow_up(issue_text) and last_issue:
#         return advanced_troubleshooting(last_issue)
#
#     doc, score = retrieve_documents(issue_text)
#
#     # ✅ NO KB MATCH → ALWAYS GEMINI
#     if not doc:
#
#         gemini_response = ask_gemini(user_problem)
#
#         # ✅ ONLY fallback if Gemini fails
#         if gemini_response.startswith("⚠"):
#
#             response = (
#                 "⚠ AI service temporarily unavailable.\n"
#                 "Switching to local diagnostic intelligence.\n\n"
#                 "Suggested Fix:\n"
#                 "1. Restart the device\n"
#                 "2. Update system drivers\n"
#                 "3. Run built-in diagnostics\n"
#                 "4. Check hardware connections\n"
#             )
#
#             return response, last_issue
#
#         # ✅ GEMINI SUCCESS
#         response = (
#             "🤖 AI Assistance\n\n"
#             + gemini_response
#         )
#
#         return response, last_issue
#
#     # ✅ KB MATCH FOUND
#     severity = format_severity(doc["severity"])
#
#     response = build_basic_response(doc, severity, score)
#
#     return response, doc["issue"]
#
#
# def build_basic_response(doc, severity, score):
#
#     response = f"{severity} {format_confidence(score)}\n\nSuggested Fix:\n"
#
#     for i, sol in enumerate(doc["solutions"], start=1):
#         response += f"{i}. {sol}\n"
#
#     return response
#
#
# def advanced_troubleshooting(issue):
#
#     response = (
#         f"I understand the issue is still unresolved ({issue}).\n\n"
#         "Advanced Troubleshooting Steps:\n"
#         "1. Run full hardware diagnostics\n"
#         "2. Reinstall related drivers\n"
#         "3. Check OS-level conflicts\n"
#         "4. Test in Safe Mode\n"
#         "5. Verify recent updates / changes\n"
#         "6. Escalate to IT / hardware support if needed"
#     )
#
#     return response, issue