def count_marketers(
        job_titles: list[str]
) -> int: 
    if not job_titles:
        return 0

    count = 0
    if job_titles[-1].lower() == "marketer":
        count += 1

    count += count_marketers(job_titles[:-1])

    return count

