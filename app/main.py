def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"], #18
        "column": error["column_number"], #80
        "message": error["text"], #"line too long (99 > 79 characters)",
        "name": error["code"],
        "source": "flake8"
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [format_linter_error(err) for err in errors],
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(key, value)
        for key, value in linter_report.items()
    ]