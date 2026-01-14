#!/usr/bin/env python3
"""
Legal Documentation Scraper
Extracts contract terms, legal obligations, and compliance issues
Focus: JOC contracts, Public Contract Code compliance
"""

import json
import re
from datetime import datetime
from typing import Dict, List

class LegalDocumentsScraper:
    """
    Extracts and analyzes legal documents and contract terms
    """
    
    def __init__(self):
        self.jurisdiction = "Contra Costa County, California"
        self.contract_type = "Job Order Contract (JOC)"
        self.legal_framework = [
            "California Public Contract Code",
            "California Civil Code (Prompt Payment Act)",
            "Federal Labor Code",
            "Government Code"
        ]

    def extract_aztec_contract_terms(self) -> Dict:
        """
        Extract terms from Aztec JOC-018 contract (Example Contract provided)
        """
        contract = {
            "form": "CC-1 (Contra Costa County Standard Form)",
            "form_approval": "Rev. 2-07",
            "parties": {
                "public_agency": "CONTRA COSTA COUNTY",
                "contractor": "Aztec Consultants, Inc.",
                "contractor_address": "2021 Omega Road, Ste 200, San Ramon, CA 94583"
            },
            "contract_number": "000-1901",
            "joc_designation": "JOB ORDER CONTRACT - 018",
            "authorization_number": "WW1006",
            "effective_date": "November 2, 2021",
            "contract_type": "Construction Agreement - Job Order Contract",
            "key_terms": {
                "maximum_value": "$3,000,000.00",
                "minimum_value": "$25,000.00",
                "contract_duration": "1 year (365 days) or maximum contract value, whichever comes first",
                "notice_to_proceed": "Required for each individual Job Order",
                "federal_tax_id": "68-0262823"
            },
            "county_contacts": {
                "public_agency_agent": "Warren Lai, Deputy Public Works Director",
                "capital_projects_manager": "Ramesh Kanzaria, Capital Projects Division Manager"
            },
            "payment_terms": {
                "frequency": "1st of each calendar month",
                "payment_basis": "Work completed through 15th of preceding month",
                "retention": "5% per Public Contract Code Section 9203",
                "final_payment": "35 calendar days after completion notice"
            },
            "insurance_requirements": {
                "basis": "Labor Code Sections 1860-61",
                "requirement": "Workers' Compensation insurance",
                "labor_code_compliance": "Section 3700"
            },
            "wage_requirements": {
                "basis": "Labor Code Section 1773",
                "requirement": "Prevailing wage rates per Department of Industrial Relations",
                "daily_work": "8 hours constitutes legal day",
                "overtime_compliance": "Labor Code Sections 1810-1815"
            },
            "important_sections": {
                "section_6_payment": "County pays for strict performance as determined by Public Agency",
                "section_7_withholding": "County may withhold payment for defective work or claims",
                "section_11_laws": "Labor Code Sections 1775, 1813 (prevailing wages), 1776 (payroll records)",
                "section_20_venue": "Litigation venue: Contra Costa County (contractor waives removal)",
                "section_22_record_retention": "5-year record retention requirement"
            },
            "liquidated_damages": {
                "applicability": "If contractor fails to complete within time fixed",
                "schedule_example": {
                    "1_to_25k": "$235/day",
                    "25k_to_100k": "$325/day",
                    "100k_to_250k": "$410/day",
                    "250k_to_500k": "$525/day",
                    "500k_to_1m": "$750/day"
                }
            }
        }
        return contract

    def extract_payment_law_compliance(self) -> Dict:
        """
        Extract California Prompt Payment Act requirements
        Based on Mike Vila's legal correspondence
        """
        payment_law = {
            "statute": "California Civil Code Section 8800 et seq. (Prompt Payment Act)",
            "applicability": "Public entity construction contracts",
            "key_sections": {
                "8800": "General Prompt Payment requirements",
                "8812": {
                    "title": "Payment by Public Entities",
                    "requirement": "Payment within 30 days of receiving demand",
                    "exceptions": "As otherwise agreed in writing",
                    "applicability": "Original contractor progress billings"
                },
                "8814": {
                    "title": "Dispute Withholding",
                    "requirement": "Public entity may withhold no more than 150% of disputed amount",
                    "principle": "Undisputed work must be paid timely"
                },
                "8818": {
                    "title": "Interest Penalty",
                    "interest_rate": "2% per month on unpaid balance",
                    "trigger": "Payment not made within Section 8812 timeframe",
                    "applicability": "All overdue undisputed amounts"
                },
                "20104.50": {
                    "statute": "Public Contract Code Section 20104.50",
                    "title": "Payment Timelines for JOC Contracts",
                    "applicability": "Specific to Job Order Contracts",
                    "referenced_in": "County correspondence to MVP (June 2024)"
                }
            },
            "mvc_application": {
                "invoices_disputed": ["023-007-004", "023-007-006", "023-007-007"],
                "legal_basis_cited": "California Prompt Payment Act, Sections 8800-8818",
                "county_acknowledgment": "County agreed to audit payment timelines (June 26, 2024)",
                "county_action": "Submitted interest payment request to Auditor's Office (July 17, 2024)",
                "result": "Interest calculated and processed per Section 8818"
            }
        }
        return payment_law

    def extract_contract_code_requirements(self) -> Dict:
        """
        Extract California Public Contract Code requirements
        """
        pcc_requirements = {
            "fair_distribution": {
                "principle": "Public agencies must ensure equitable work distribution",
                "sections": ["4100-4114", "20104.50"],
                "transparency_requirement": "Work must be distributed fairly among qualified contractors",
                "mvc_concern": "Same 2 contractors receiving 90%+ of work across multiple JOC cycles"
            },
            "minimum_obligation": {
                "interpretation_county": "County has minimum obligation only",
                "mvc_argument": "Fairness and transparency require equitable distribution",
                "legal_standard": "California Public Contract Code principles"
            },
            "subcontractor_sections": "Sections 4100-4114 incorporated by reference",
            "wage_compliance": "Department of Industrial Relations prevailing wage certification",
            "venue_provision": "Work shall be performed in Contra Costa County"
        }
        return pcc_requirements

    def extract_disputed_projects(self) -> Dict:
        """
        Extract details of disputed projects from legal correspondence
        """
        disputed = {
            "30_muir_road_project": {
                "location": "30 Muir Road, Martinez, CA 94553",
                "owner": "Contra Costa County",
                "contractor": "M V P Construction LLC",
                "project_manager": "Brendan Havenar-Daughton (Energy Manager)",
                "dispute_type": "Scope reconciliation",
                "dispute_duration": {
                    "start": "December 2023",
                    "current": "February 2024+",
                    "duration_months": "2+ months"
                },
                "dispute_parties": {
                    "mvc": "Mike Vila, Owner",
                    "county_pm": "Brendan Havenar-Daughton",
                    "county_management": ["Mauricio Moreno", "Jeff Acuff"],
                    "county_consultant": "George Stavros (Gordian)"
                },
                "key_issues": [
                    "Scope of work interpretation",
                    "Measured quantities vs. contracted quantities",
                    "Additional work performed",
                    "Reconciliation calculation methodology"
                ],
                "disputed_amounts": "Estimated $40,000+ (from correspondence)",
                "supporting_documentation": [
                    "Hard copies of work order receipts",
                    "Supplier invoices",
                    "Concrete truck documentation",
                    "Supplemental cost documentation"
                ],
                "mvc_position": "Reconciliation should be 'cut both ways' (credits and debits)",
                "county_position": "Reconciliation only adjusts for scope variation, not corrective work",
                "impact": {
                    "financial_strain": "MVP covering costs upfront",
                    "subcontractor_impact": "Contractors refusing additional County work",
                    "business_reputation": "Damage to MVP relationships and bidding position"
                }
            }
        }
        return disputed

    def extract_ens_legis_framework(self) -> Dict:
        """
        Extract ENS LEGIS framework documents
        Legal foundation for digital operations
        """
        ens_legis = {
            "concept": "Ens Legis (creature of the law)",
            "definition": "Artificial being created by law, contrasted with natural person",
            "application": "Digital persona/AI clone as authorized representative",
            "legal_basis": {
                "persona_ficta": "Juridical/artificial person",
                "characteristics": [
                    "Legal rights, protections, privileges & liabilities",
                    "Can sue, be sued, enter contracts, own property",
                    "Exists solely because law creates/recognizes it"
                ]
            },
            "digital_clone_designation": "Campaign Coordinator - Incrimination Nation",
            "authorized_operations": [
                "Legal Document Management & Assembly",
                "Campaign Content Creation & Distribution",
                "Platform Integration & Automation",
                "Bot Development & Data Scraping Oversight"
            ],
            "framework_file": "Untitled dENS LEGIS FICTITIOUS PERSON - Digital Clone Framework",
            "created_date": "January 10, 2026"
        }
        return ens_legis

    def generate_legal_analysis_report(self) -> Dict:
        """
        Generate comprehensive legal analysis report
        """
        report = {
            "title": "Legal Documentation Analysis - MVP Construction vs. Contra Costa County",
            "date_generated": datetime.now().isoformat(),
            "jurisdiction": "Contra Costa County, California",
            "case_focus": [
                "JOC contract work distribution equity",
                "Payment law compliance",
                "30 Muir Road project reconciliation"
            ],
            "extracted_contracts": {
                "aztec_joc_018": self.extract_aztec_contract_terms()
            },
            "legal_requirements": {
                "payment_law": self.extract_payment_law_compliance(),
                "contract_code": self.extract_contract_code_requirements()
            },
            "disputed_matters": self.extract_disputed_projects(),
            "legal_framework": self.extract_ens_legis_framework(),
            "analysis_summary": {
                "payment_law_violations": "County acknowledged late payments, interest processed per Code 8818",
                "contract_equity_issues": "3-year pattern of inequitable work distribution documented",
                "30_muir_dispute": "Ongoing scope reconciliation with $40k+ in dispute",
                "legal_remedies_available": [
                    "Payment disputes resolved under Prompt Payment Act",
                    "Public Contract Code equity arguments supported by 3-year record",
                    "30 Muir reconciliation may require mediation or litigation"
                ]
            }
        }
        return report

    def save_report(self, report, filename="legal_analysis_extract.json"):
        """Save legal analysis to JSON"""
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        return filename


if __name__ == "__main__":
    scraper = LegalDocumentsScraper()
    report = scraper.generate_legal_analysis_report()
    scraper.save_report(report)
    print(json.dumps(report, indent=2))
