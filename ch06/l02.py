def last_work_experience(
        work_experiences: list[str]
) -> str | None:
    return None if not work_experiences else work_experiences[-1]
