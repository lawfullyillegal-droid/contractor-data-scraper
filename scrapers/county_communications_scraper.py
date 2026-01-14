#!/usr/bin/env python3
"""
Contra Costa County Communications Data Scraper
Extracts public records, email communications, and official correspondence
Focus: JOC program, Capital Projects Management Division, Public Works
"""

import json
import re
from datetime import datetime
from typing import Dict, List

class CountyOfficialsScraper:
    """
    Scrapes and organizes Contra Costa County officials and contacts
    Focus: Public Works, Capital Projects Management
    """
    
    def __init__(self):
        # County organizational structure from extracted documents
        self.county = "Contra Costa County"
        self.county_location = "Martinez, CA 94553"
        self.pw_department = "Public Works Department"
        self.pw_address = "255 Glacier Drive, Martinez, CA 94553"
        
        # Key officials and contact information
        self.officials = {
            "Jeff Acuff": {
                "title": "Division Manager",
                "department": "Capital Projects Management",
                "office_phone": "925-655-3130",  # Updated number
                "mobile": "925-595-6001",
                "email": "Jeff.Acuff@pw.cccounty.us",
                "decision_authority": "JOC contract assignments, payment approval",
                "role_notes": "Primary contact for MVP Construction concerns (2022-2025)"
            },
            "Ramesh Kanzaria": {
                "title": "Capital Projects Division Manager",
                "department": "Capital Projects Management",
                "entity": "Contra Costa County",
                "role_notes": "Historical PM for MVP projects, now retired"
            },
            "Warren Lai": {
                "title": "Deputy Public Works Director",
                "department": "Public Works",
                "email": "warren.lai@pw.cccounty.us",
                "entity": "Contra Costa County"
            },
            "Brendan Havenar-Daughton": {
                "title": "Energy Manager",
                "department": "Capital Projects Management",
                "office_phone": "925-957-2473",
                "mobile": "925-812-7703",
                "email": "Brendan.Havenar-Daughton@pw.cccounty.us",
                "role_notes": "30 Muir Road project manager, reconciliation lead"
            },
            "Mauricio Moreno": {
                "title": "Project Manager/Consultant",
                "department": "Capital Projects Management",
                "email": "Mauricio.Moreno@pw.cccounty.us",
                "role_notes": "30 Muir project, reconciliation disputed party"
            },
            "George Stavros": {
                "title": "Consultant",
                "company": "Gordian",
                "email": "G.Stavros@gordian.com",
                "role_notes": "JOC program consultant, contractor evaluation specialist"
            }
        }

    def scrape_communication_records(self) -> Dict:
        """
        Extract communication records and correspondence patterns
        Source: Email chain analysis from provided documents
        """
        records = {
            "communication_thread_1": {
                "subject": "JOC 012, 013, 014, 015 & 016 / JOC 017, 018, 019, 020",
                "date_initiated": "2022-01-28",
                "initiator": "Mike Vila, MVP Construction",
                "recipient": "admin@pw.cccounty.us",
                "cc": ["warren.lai@pw.cccounty.us"],
                "key_points": [
                    "MVP alleges unequal work distribution",
                    "Two contractors (Aztec, Mark Scott) heavily favored",
                    "MVP received only 2 RFPs in first JOC",
                    "MVP revenue: $250k, bonding costs: $30k",
                    "County's minimum obligation met, equity not addressed",
                    "Public Records Request filed"
                ],
                "status": "Acknowledged by County, no resolution"
            },
            "communication_thread_2": {
                "subject": "Contract Timeline and RFP Opportunities – JOC 025",
                "date_initiated": "2025-01-27",
                "initiator": "Mike Vila, MVP Construction",
                "recipient": "Jeff Acuff",
                "key_points": [
                    "JOC-025 contract dates confirmed: 2024-07-29 to 2025-10-26",
                    "MVP concerns about equitable work distribution continue",
                    "Aztec and Mark Scott again dominating contract awards",
                    "Aztec contract doubled: $2.5M to $5M",
                    "MVP never completed 50% of awarded contract value",
                    "Equity under California Public Contract Code questioned"
                ],
                "official_response": "County evaluates 'best fit' based on prior performance",
                "resolution": "Pending - pattern continues 3 years later"
            },
            "communication_thread_3": {
                "subject": "Reconciliation Next Steps - 30 Muir Road Project",
                "date_initiated": "2024-02-01",
                "parties": ["Mike Vila", "Brendan Havenar-Daughton", "Jeff Acuff", "Mauricio Moreno"],
                "duration": "2 months (Dec 2023 - Feb 2024)",
                "key_issues": [
                    "Scope dispute on 30 Muir Road project",
                    "Delayed feedback and payment processing",
                    "County consultant (George) involvement disputed",
                    "Subcontractor relationships strained due to County PM behavior",
                    "Payment reconciliation stuck since December 2023",
                    "Mike Vila requests direct intervention from Jeff Acuff"
                ],
                "disputed_amount_estimated": "$40,000+",
                "key_quote_county": "'Reconciliation is not intended to pay for corrective work'",
                "resolution_status": "Unresolved as of communication date"
            },
            "communication_thread_4": {
                "subject": "Invoice Payment and California Prompt Payment Act Compliance",
                "date_initiated": "2024-01-16",
                "initiator": "Mike Vila",
                "recipient": ["Jeff Acuff", "Susan Lindstrom"],
                "disputed_invoices": [
                    "Invoice #023-007-004",
                    "Invoice #023-007-006",
                    "Invoice #023-007-007"
                ],
                "legal_basis": "California Civil Code Section 8800 et seq. (Prompt Payment Act)",
                "key_points": [
                    "30-day payment requirement violated",
                    "Interest accrual at 2% per month on unpaid balance",
                    "County acknowledges Public Contract Code 20104.50 obligations",
                    "Payment eventually processed with interest accrual",
                    "Pattern of late payments documented"
                ],
                "county_action": "Submitted interest payment request to Auditor's Office (July 2024)",
                "resolution": "Partial - interest calculated and processed"
            }
        }
        return records

    def extract_contract_identifiers(self) -> Dict:
        """
        Extract all contract and project identifiers from communications
        """
        identifiers = {
            "joc_contracts": {
                "joc_012_016": {
                    "status": "Historical",
                    "mvc_performance": "$250k revenue, negative ROI"
                },
                "joc_017_020": {
                    "status": "Historical",
                    "mvc_performance": "$0 revenue",
                    "other_contractors": {
                        "Mark Scott Construction": "$1,879,526.93",
                        "Aztec Consultants": "$2,238,389.05",
                        "MIK Construction": "$318,702.15"
                    }
                },
                "joc_022": {
                    "status": "Historical",
                    "mvc_performance": "Unknown revenue"
                },
                "joc_025": {
                    "status": "Current",
                    "start_date": "2024-07-29",
                    "end_date": "2025-10-26",
                    "mvc_status": "Awarded, low initial RFP activity"
                }
            },
            "specific_projects": {
                "30_muir_road": {
                    "location": "30 Muir Road, Martinez, CA",
                    "project_type": "County facility",
                    "contractor": "MVP Construction",
                    "dispute_period": "Dec 2023 - Feb 2024+",
                    "key_personnel": "Mike Vila (owner), Brendan Havenar-Daughton (PM)",
                    "status": "Reconciliation dispute ongoing"
                }
            },
            "financial_identifiers": {
                "taxpayer_id_aztec": "68-0262823",
                "wbe_license_mvc": "1047890",
                "mvc_business_license": "MVP Construction LLC"
            }
        }
        return identifiers

    def scrape_public_records_data(self) -> Dict:
        """
        Extract data that would be available through public records requests
        """
        public_data = {
            "job_order_tracking_reports": {
                "report_date": "2022-12-09",
                "source": "Contra Costa County Public Works",
                "joc_017_mark_scott": {
                    "total_issued": "$1,879,526.93",
                    "sample_projects": [
                        {"jo_id": "J17-02-250-22009-W", "title": "Lab Building Parking Lot Modification", "amount": "$313,519.21"},
                        {"jo_id": "J17-03-250-2013-WH", "title": "10 Douglas Drive FLIP Generator", "amount": "$615,197.56"},
                        {"jo_id": "J17-04-250-1803-WH", "title": "CCRMC Pharmacy Compounding Room Upgrade", "amount": "$113,422.53"}
                    ]
                },
                "joc_018_aztec": {
                    "total_issued": "$2,238,389.05",
                    "sample_projects": [
                        {"jo_id": "J18-01-345-2101-WH", "title": "Pittsburg Health Center Cooling Tower Replacement", "amount": "$988,469.46"},
                        {"jo_id": "J18-02-250-22010-W", "title": "CCRMC Parking Lot Repair-Seal Coat", "amount": "$444,459.45"},
                        {"jo_id": "J18-03-WON:6643271-WH", "title": "WCDF Walk-In Refrigerator & Freezer Replacement", "amount": "$763,687.94"}
                    ]
                },
                "joc_020_mvp_construction": {
                    "total_issued": "$0.00",
                    "note": "Proposal Review stage, no completed work"
                }
            }
        }
        return public_data

    def generate_complete_report(self) -> Dict:
        """
        Generate comprehensive scraper report with all extracted data
        """
        report = {
            "title": "Contra Costa County Communications & Contracts Data Extract",
            "date_generated": datetime.now().isoformat(),
            "data_sources": [
                "Email communications (Jan 2022 - Jan 2025)",
                "Job Order Tracking Reports",
                "Public Records Requests",
                "County official contact directories"
            ],
            "extracted_data": {
                "officials": self.officials,
                "communications": self.scrape_communication_records(),
                "contracts": self.extract_contract_identifiers(),
                "public_records": self.scrape_public_records_data()
            },
            "analysis_notes": [
                "Pattern of inequitable work distribution documented",
                "Two contractors (Aztec, Mark Scott) receive ~90% of work",
                "MVP concerns raised consistently over 3+ years",
                "Payment disputes indicate cash flow impact on contractor",
                "30 Muir Road reconciliation represents current dispute focus"
            ]
        }
        return report

    def save_report(self, report, filename="county_communications_extract.json"):
        """Save extracted data to JSON"""
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        return filename


if __name__ == "__main__":
    scraper = CountyOfficialsScraper()
    report = scraper.generate_complete_report()
    scraper.save_report(report)
    print(json.dumps(report, indent=2))
