from flask import Blueprint, request

from app.services.report_service import ReportService

bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/api/v1/reports"
)

@bp.get("")
def get_reports():

    reports = ReportService.get_all()

    return {
        "success": True,
        "data": [
            report.to_dict()
            for report in reports
        ]
    }, 200

@bp.get("/<int:report_id>")
def get_report(report_id):

    report = ReportService.get_by_id(report_id)

    return {
        "success": True,
        "data": report.to_dict()
    }, 200

@bp.post("")
def create_report():

    data = request.get_json()

    try:

        report = ReportService.create(data)

        return {
            "success": True,
            "message": "Report submitted successfully",
            "data": report.to_dict()
        }, 201

    except ValueError:
        return {
            "success": False,
            "message": "Invalid CSK ID"
        }, 400

@bp.put("/<report_id>/status")
def update_status(report_id):

    data = request.get_json()

    print(f"data = {data}")

    report = ReportService.update_status(
        report_id,
        data["status"]
    )

    return {
        "success": True,
        "message": "Status updated successfully",
        "data": report.to_dict()
    }, 200

@bp.delete("/<report_id>")
def delete_report(report_id):

    print(f"type = {type(report_id)}")

    ReportService.delete(report_id)

    return {
        "success": True,
        "message": "Report deleted successfully"
    }, 200