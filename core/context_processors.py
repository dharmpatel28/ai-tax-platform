def user_role(request):

    return {
        "role": request.session.get(
            "user_role",
            "client"
        )
    }