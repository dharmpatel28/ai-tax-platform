from django.shortcuts import render, redirect

from .utils.json_loader import load_json

import json
from pathlib import Path


def landing(request):
    role = request.session.get("role")
    
    if role:
        request.session["user_role"] = role
        request.session.modified = True

    return render(request, "landing.html")


def select_role(request, role):
    request.session["role"] = role
    request.session["user_role"] = role
    request.session.modified = True

    print("ROLE SET TO:", role)

    if role == "client":
        return redirect("client_dashboard")

    return redirect("cpa_dashboard")

def client_dashboard(request):

    role = request.session.get("role")
    
    if role:
        request.session["user_role"] = role
        request.session.modified = True

    return render(request, "client/dashboard.html", {
        "role": "client"
    })


# def cpa_dashboard(request):

#     request.session["role"] = "cpa"

#     return render(request, "cpa/dashboard.html", {
#         "role": "cpa"
#     })

def cpa_dashboard(request):

    role = request.session.get("role")
    
    if role:
        request.session["user_role"] = role
        request.session.modified = True

    priority_tasks = [

        {
            "id": 1,
            "client": "John Doe",
            "issue": "Missing Mortgage Document",
            "owner": "Client",
            "priority": "High",
            "status": "Waiting"
        },

        {
            "id": 2,
            "client": "Sarah Smith",
            "issue": "AI Finding Needs Approval",
            "owner": "CPA",
            "priority": "Medium",
            "status": "Review"
        },

        {
            "id": 3,
            "client": "Mike Johnson",
            "issue": "Return Ready For Submission",
            "owner": "CPA",
            "priority": "Low",
            "status": "Complete"
        }

    ]

    summary = {

        "pending_returns": 5,

        "missing_documents": 3,

        "ai_reviews": 2,

        "client_actions": 4

    }

    return render(
        request,
        "cpa/dashboard.html",
        {
            "priority_tasks": priority_tasks,
            "summary": summary
        }
    )


def returns_list(request):

    role = request.session.get("role")

    if role:
        request.session["user_role"] = role
        request.session.modified = True

    print("=" * 40)
    print("ROLE:", role)
    print("=" * 40)

    print("SESSION:", dict(request.session))
    print("ROLE:", request.session.get("role"))

    with open("core/mock_data/returns.json") as f:
        returns = json.load(f)

    if role == "client":
        print("Loading CLIENT template")
        return render(
            request,
            "client/returns.html",
            {"returns": returns},
        )

    print("Loading CPA template")
    return render(
        request,
        "cpa/returns.html",
        {"returns": returns},
    )


def return_detail(request, return_id):

    role = request.session.get("role")
    
    if role:
        request.session["user_role"] = role
        request.session.modified = True

    with open("core/mock_data/returns.json") as f:
        returns = json.load(f)

    with open("core/mock_data/ai_reviews.json") as f:
        reviews = json.load(f)

    current_return = next(
        r for r in returns
        if r["id"] == return_id
    )

    return_reviews = [
        r for r in reviews
        if r["return_id"] == return_id
    ]

    context = {
        "return": current_return,
        "reviews": return_reviews,
    }

    return render(
        request,
        "cpa/return_detail.html",
        context,
    )


def document_detail(request, document_id):

    role = request.session.get("role")
    
    if role:
        request.session["user_role"] = role
        request.session.modified = True

    documents = load_json("documents.json")

    document = next(
        (d for d in documents if d["id"] == document_id),
        None
    )

    return render(
        request,
        "cpa/document_detail.html",
        {
            "document": document
        }
    )


def returns(request):

    role = request.session.get("role")

    if role:
        request.session["user_role"] = role
        request.session.modified = True

    if role == "client":
        # Later you can filter to only the logged-in client's returns
        return render(
            request,
            "client/returns.html",
            {"returns": returns}
        )

    return render(
        request,
        "cpa/returns.html",
        {"returns": returns}
    )


def documents(request):
    role = request.session.get("role")

    if role:
        request.session["user_role"] = role
        request.session.modified = True

    documents = load_json("documents.json")

    if role == "cpa":
        template = "cpa/document.html"
    else:
        template = "client/documents.html"

    return render(request, template, {
        "role": role,
        "documents": documents
    })


def messages(request):

    role = request.session.get("role")

    if role:
        request.session["user_role"] = role
        request.session.modified = True

    if role == "cpa":
        template = "cpa/messages.html"

    else:
        template = "client/messages.html"

    return render(
        request,
        template,
        {
            "role": role
        }
    )


def ai_review(request):

    role = request.session.get("role")

    if role:
        request.session["user_role"] = role
        request.session.modified = True

    if role == "cpa":
        template = "cpa/ai_review.html"
    else:
        template = "client/ai_review.html"

    return render(request, template, {
        "role": role
    })


def ai_review_detail(request, id):

    role = request.session.get("role")
    
    if role:
        request.session["user_role"] = role
        request.session.modified = True

    return render(
        request,
        "cpa/ai_review_detail.html",
        {
            "return_id": id
        }
    )


def status(request):

    role = request.session.get("role")

    if role:
        request.session["user_role"] = role
        request.session.modified = True

    if role == "cpa":
        template = "cpa/status.html"
    else:
        template = "client/status.html"

    return render(request, template, {
        "role": role
    })


def client_ai_chat(request):

    role = request.session.get("role")
    
    if role:
        request.session["user_role"] = role
        request.session.modified = True

    return render(
        request,
        "client/ai_chat.html",
        {
            "role": "client"
        }
    )


def return_workplace(request, id):

    role = request.session.get("role")
    
    if role:
        request.session["user_role"] = role
        request.session.modified = True

    return_data = {

        "id": id,
        "client": "John Doe",
        "tax_year": "2026",
        "status": "Waiting for Document",
        "next_owner": "Client",
        "next_action": "Upload Mortgage Form 1098"

    }

    traceability = [

        {
            "field": "Wages",
            "value": "$85,000",
            "document": "W2.pdf",
            "location": "Page 1 - Box 1",
            "transform": "OCR Extraction",

            "ai_generated": True,
            "editable": False,
            "verified": True,
            "approval": False
        },


        {
            "field": "Federal Tax Withheld",
            "value": "$12,500",
            "document": "W2.pdf",
            "location": "Page 1 - Box 2",
            "transform": "Currency Normalization",

            "ai_generated": True,
            "editable": True,
            "verified": True,
            "approval": False
        },


        {
            "field": "Mortgage Interest",
            "value": "$8,200",
            "document": "1098.pdf",
            "location": "Page 2 - Interest Section",
            "transform": "Deduction Mapping",

            "ai_generated": True,
            "editable": False,
            "verified": False,
            "approval": True
        }

    ]

    return render(
        request,
        "cpa/return_workplace.html",
        {
            "return_data": return_data,
            "traceability": traceability
        }
    )
