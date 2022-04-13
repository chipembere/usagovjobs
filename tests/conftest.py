import json
import pytest

from unittest import mock

from usagovjobs import constants

api_response = {
    "LanguageCode": "EN",
    "SearchParameters": {},
    "SearchResult": {
        "SearchResultCount": 2,
        "SearchResultCountAll": 2167,
        "SearchResultItems": [
            {
                "MatchedObjectId": "645184400",
                "MatchedObjectDescriptor": {
                    "PositionID": "DCSA-22-11428309-P",
                    "PositionTitle": "COMPUTER SCIENTIST (DATA SCIENTIST/DATA ANALYST)",
                    "PositionURI": "https://www.usajobs.gov:443/GetJob/ViewDetails/645184400",
                    "ApplyURI": [
                        "https://www.usajobs.gov:443/GetJob/ViewDetails/645184400?PostingChannelID="
                    ],
                    "PositionLocationDisplay": "Multiple Locations",
                    "PositionLocation": [
                        {
                            "LocationName": "Fort Meade, Maryland",
                            "CountryCode": "United States",
                            "CountrySubDivisionCode": "Maryland",
                            "CityName": "Fort Meade, Maryland",
                            "Longitude": -76.7419,
                            "Latitude": 39.1014
                        },
                        {
                            "LocationName": "Boyers, Pennsylvania",
                            "CountryCode": "United States",
                            "CountrySubDivisionCode": "Pennsylvania",
                            "CityName": "Boyers, Pennsylvania",
                            "Longitude": -79.89917,
                            "Latitude": 41.108505
                        },
                        {
                            "LocationName": "Arlington, Virginia",
                            "CountryCode": "United States",
                            "CountrySubDivisionCode": "Virginia",
                            "CityName": "Arlington, Virginia",
                            "Longitude": -77.086296,
                            "Latitude": 38.89051
                        },
                        {
                            "LocationName": "Quantico, Virginia",
                            "CountryCode": "United States",
                            "CountrySubDivisionCode": "Virginia",
                            "CityName": "Quantico, Virginia",
                            "Longitude": -77.2909,
                            "Latitude": 38.5221
                        }
                    ],
                    "OrganizationName": "Defense Counterintelligence and Security Agency",
                    "DepartmentName": "Department of Defense",
                    "JobCategory": [
                        {
                            "Name": "Computer Science",
                            "Code": "1550"
                        }
                    ],
                    "JobGrade": [
                        {
                            "Code": "GG"
                        }
                    ],
                    "PositionSchedule": [
                        {
                            "Name": "Full-time",
                            "Code": "1"
                        }
                    ],
                    "PositionOfferingType": [
                        {
                            "Name": "Permanent",
                            "Code": "15317"
                        }
                    ],
                    "QualificationSummary": "This position has a Basic Requirement for the 1550:\nBachelor's degree in computer science or bachelor's degree with 30 semester hours in a combination of mathematics, statistics, and computer science. At least 15 of the 30 semester hours must have included any combination of statistics and mathematics that included differential and integral calculus. All academic degrees and course work must be from accredited or pre-accredited institutions.\n*NOTE: Failure to provide transcripts will result in you being rated ineligible for this position. The experience described in your resume will be evaluated and screened from the Office of Personnel Management's (OPMs) basic qualifications requirements. See: Computer Science Series 1550 (opm.gov) i.e. for professional positions or positions with a basic education requirement: General Schedule Qualification Standards (opm.gov) for OPM qualification standards, competencies and specialized experience needed to perform the duties of the position as described in the MAJOR DUTIES and QUALIFICATIONS sections of this announcement by 04/14/2022 Applicant must have directly applicable experience that demonstrates the possession of the knowledge, skills, abilities and competencies necessary for immediate success in the position. Qualifying experience may have been acquired in any public or private sector job, but will clearly demonstrate past experience in the application of the particular competencies/knowledge, skills and abilities necessary to successfully perform the duties of the position. You must have specialized experience sufficient to demonstrate that you have acquired all the competencies necessary to perform at a level equivalent in difficulty, responsibility, and complexity to the next lower grade (GS/GG-12) in the Federal service and are prepared to take on greater responsibility. Generally, this would include one year or more of such specialized experience. Specialized experience for this position includes:\nSpecialized experience for this position includes principles of data science, data engineering, and/or data architecture. This experience is typically demonstrated by evidence of development of Ai/ML/NLP constructs/algorithms using python; experience using statistical software such as SPSS or SAS; experience using robotic process automation (RPA) software such as UiPath; and/or experience designing and/or implementing cloud based big data stores optimized for Ai. Specifically you will be evaluated on the following competencies: 1. Data Analysis - Manipulate and exploit internal and external, structured, and unstructured data sources to accomplish organizational goals. 2. Modeling and Simulation - Apply tools, techniques, and procedures to develop functional, physical, or prototype models and simulations for training, testing and evaluation, the prediction of behavior and phenomena, the evaluation of design alternatives, to support operational preparation, and to visually communicate concepts and/or validate requirements. 3. Programming Languages - Use programming languages to script and automate tasks; applies programming languages and skills across multiple platforms or frameworks. 4. Software Engineering - Designs software utilizing the software life cycle process; develops, deploys, updates, maintains, and tests software using methodologies and tools; designs to leverage software reusability; and establishes and utilizes software engineering metrics. 5. Systems Design - Design and evaluate software and hardware and develops enterprise and solution architectures that meet user needs and optimize performance, using applicable principles, methods, and tools.",
                    "PositionRemuneration": [
                        {
                            "MinimumRange": "97738.0",
                            "MaximumRange": "138868.0",
                            "RateIntervalCode": "Per Year"
                        }
                    ],
                    "PositionStartDate": "2022-03-25T11:18:12.4200",
                    "PositionEndDate": "2022-04-14T23:59:59.9970",
                    "PublicationStartDate": "2022-03-25T11:18:12.4200",
                    "ApplicationCloseDate": "2022-04-14T23:59:59.9970",
                    "PositionFormattedDescription": [
                        {
                            "Label": "Dynamic Teaser",
                            "LabelDescription": "Hit highlighting for keyword searches."
                        }
                    ],
                    "UserArea": {
                        "Details": {
                            "JobSummary": "This position is placed in the Program Executive Office (PEO) or one of DCSA's Mission or Mission Support Areas. There are multiple vacancies in the Program Executive Office (PEO). The individual will serve as a Data Scientist, Data Engineer, or Data Architect under the Office of the Technical Director (OTD) or directly for one of the Program Managers (PM), supporting one or more of DCSA's missions.",
                            "WhoMayApply": {
                                "Name": "",
                                "Code": ""
                            },
                            "LowGrade": "13",
                            "HighGrade": "13",
                            "PromotionPotential": "None",
                            "OrganizationCodes": "DD/DD12",
                            "Relocation": "True",
                            "HiringPath": [
                                "public"
                            ],
                            "TotalOpenings": "13",
                            "AgencyMarketingStatement": "Mission Statement\nThe Defense Counterintelligence and Security Agency (DCSA) is a separate Agency of the Department of Defense (DoD) under the direction, authority, and control of the Under Secretary of Defense for Intelligence and Security (USD (I&S). The mission of the DCSA is as follows: -Deliver efficient and effective background investigations, adjudications and continuous vetting to safeguard the integrity and trustworthiness of an agile federal and contractor workforce, and preserve military readiness and warfighting capabilities\n-Identify and neutralize foreign intelligence threats to the USG's trusted workforce and critical technologies\n-Develop and articulate holistic threat picture of risk posed by foreign intelligence entities and hostile insiders, enabling the USG to strengthen our security posture, continuously protect against the evolving threat, and enable action agencies to more effectively counter adversaries\n-Contribute meaningful analysis to the Intelligence Community (IC)-Manage the National Industrial Security Program (NISP) on behalf of the Secretary of Defense by clearing industrial facilities, personnel, and associated IT systems\n-Identify and defeat threats presented to critical technologies and through the supply chain\n-Provide education, training, research, and security awareness to DoD, other federal government organizations, and industry\n-Execute enterprise management responsibilities for DoD Security and Insider Threat Programs.",
                            "TravelCode": "1",
                            "ApplyOnlineUrl": "https://apply.usastaffing.gov/Application/Apply",
                            "DetailStatusUrl": "https://apply.usastaffing.gov/Application/ApplicationStatus",
                            "MajorDuties": [
                                "As a COMPUTER SCIENTIST (DATA SCIENTIST/DATA ANALYST) you will be responsible for the following duties: Responsible for the application of data science principals, planning, executing, and implementing various data curation, acquisition, analytic, and delivery functions that support the work of the DCSA's Enterprise Architecture and the mission and business functions it supports. The position will support a number of efforts across DCSA including Personnel Vetting, Industrial Security, Insider Threat, Security Education & Training and Counterintelligence. The position may interact with one or more of DCSA's research and innovation partners, and the missions they support. Researches and oversees implementation of capabilities solutions to solve agency business problems. Pans, describes and/or develops computer programs required to keep existing software responsive to constant changing data requirements. Responsible for developing program and agency plans, describes and/or develops computer programs required to keep existing software responsive to constant changing data requirements. Serves as a catalyst for creative engineering/computer scientist thinking to integrate new technology capabilities and opportunities to develop more effective and responsive intelligence. The encumbent will complete these activities utilizing expertise within software-system engineering, artificial intelligence (Ai) and machine learning (ML), Information Technology Architecture, and other related disciplines."
                            ],
                            "Education": "Substitution of education may not be used in lieu of specialized experience for this grade level. Must have a bachelor's degree in computer science or bachelor's degree with 30 semester hours in a combination of mathematics, statistics, and computer science. At least 15 of the 30 semester hours must have included any combination of statistics and mathematics that included differential and integral calculus. All academic degrees and course work must be from accredited or pre-accredited institutions.",
                            "Requirements": "",
                            "Evaluations": "Once the application process is complete, your resume and supporting documentation will be used to determine whether you meet the job qualifications listed on this announcement. If you are minimally qualified for this job, your resume and supporting documentation will be compared to your responses on the Occupational Questionnaire. If you rate yourself higher than is supported by your application materials, your responses may be adjusted and/or you may be excluded from consideration for this job If you are found to be among the top candidates, you will be referred to the selecting official for employment consideration.",
                            "HowToApply": "To apply for this position, you must provide a complete Application Package as described in REQUIRED DOCUMENTS. Click 'Apply Online' to create an account or log in to your existing USAJOBS account. 1. Follow the prompts to complete the assessment questionnaire and upload required documents.\n2. Please ensure you click the Submit My Answers button to submit your application.\n3. Applications must be received by the closing date of the announcement to receive consideration. To review the status of an application through USAJOBS: 1. Log into your USAJOBS account\n2. Click Application Status within your profile to expand your application\n3. Locate the job announcement and click the more information link under the Status column for this position. You will be routed to Application Manager. The Details tab displays by default. The Details tab displays comprehensive information about the selected Application Package including: assessment(s) and the status, supporting documents and their status, correspondence sent to you by the hiring agency, and your application processing status.",
                            "WhatToExpectNext": "Once you successfully complete the application process, you will receive a notification of receipt. Your application package will be reviewed to ensure you meet the basic eligibility and qualifications requirements, and you will receive a notification. A review will be made of your online questionnaire and the documentation you submitted to support your responses. A list of qualified applicants will be created and sent to the selecting official. All applicants reviewed and/or referred will receive a notification letter. The selecting official may choose to conduct interviews, and once the selection is made, you will receive a notification of the decision. *NOTE: If you submit a resume but no questionnaire, you cannot be considered for the position. If you submit a questionnaire but no resume, you cannot be considered for the position. Your application will be appropriately documented and you will be removed from further competition against this announcement. REGARDING INTERVIEWS: Interviews may be required for this position. Accommodations may be made to conduct telephonic interviews to preclude travel hardships for applicants. Note: Declining to be interviewed or failure to report for a scheduled interview will be considered as a declination for further consideration for employment against this vacancy.\nThe Defense Counterintelligence and Security Agency provides reasonable accommodations to applicants with disabilities. If you need a reasonable accommodation for any part of the application and hiring process, please notify the point of contact for this job announcement. Your requests for reasonable accommodation will be addressed on a case-by-case basis. This announcement may be used to fill additional vacancies.",
                            "RequiredDocuments": "Please review the General Application Information and Definitions at:\nhttps://www.dla.mil/Portals/104/Documents/Careers/downloads/DoDGenAppInfo%2012-1-2020.pdf?ver=ECNbdsHtGilTd3OENN4A0Q%3d%3d The documents you are required to submit vary based on the authority you are using to apply (i.e., applying as a veteran, applying as a current permanent Federal employee, applying as a reinstatement, etc.). Your complete application includes your COMPLETE resume, your responses to the online questionnaire, and documents which prove your eligibility to apply. If you fail to provide these documents, you will be marked as having an incomplete application package and you will not be considered any further. The following documents are REQUIRED\n1. Your resume: If area of consideration is limited to the local commuting area, you must reside OR be currently employed within a reasonable distance of the advertised position's location(s). Please ensure your resume reflects your current home address and/or employer's address as this will be used to determine the area of consideration eligibility requirement when an SF50 is not applicable Your resume may be submitted in any format. It must include your name and contact information and support the specialized experience described in this announcement. For qualifications determinations your resume must contain the dates of employment (i.e., Month/Year to present). For additional information see: What to include in your resume. 2. Transcripts This position has a degree or education requirement so you are required to submit a copy of your transcript College transcript(s), required if qualifying based on education. We accept unofficial transcripts, as long as they contain your name, the name of the school, the date and degree that was awarded, and the lists of classes and credits earned. 3. Veteran's Documents If applying for Veteran's preference, please provide a copy of your DD214 showing character of service, SF-15 Form and VA letter showing final percentage, or certification of expected discharge or release from active duty. Future Military Retirees: You are required to submit a copy of your \"official\" Retirement (NOTE: Member 4 Copy is preferred, but we will accept copies that show character of service i.e. \"honorable or general-under honorable conditions.\" The Member 1 copy will not be accepted), OR if your DD214 has yet to be approved, a Retirement Letter will be accepted up to 120 days prior to retirement signed by, or by direction of, the adjutant, personnel officer, or commander of your unit or higher headquarters which must include your rank, dates of active duty service, the Type of Discharge, Character of Service (i.e. honorable). IF, you are taking leave prior to your retirement date, you must provide a copy of your \"approved\" terminal leave request form (must show \"Terminal\" or \"Other- Transition\") or the Approved Terminal/Other-Transition Leave Start Date must be indicated on your Retirement Letter. If you are not taking leave prior to your separation date you are not required to provide a terminal leave request form or indicate a Leave Start Date on your Statement of Service. Future Military Separatees (Not Retiring): You are required to submit a copy of your \"official\" DD214 (NOTE: Member 4 Copy is preferred, but we will accept copies that show character of service i.e. \"honorable or general-under honorable conditions.\" The Member 1 copy will not be accepted), OR if your DD214 has yet to be approved, a copy of your most recent active duty orders for separation or a statement of service letter will be accepted up to 120 days prior to separation which must reflect the Type of Discharge, and Character of Service (i.e. honorable). IF, you are taking leave prior to your separation date, you must provide a copy of your \"approved\" terminal leave request form (must show \"Terminal\" or \"Other-Transition\") or the Approved Terminal/Other-Transition Leave Start Date must be indicated on your Statement of Service. If you are not taking leave prior to your separation date you are not required to provide a terminal leave request form or indicate a Leave Start Date on your Statement of Service. NOTE: Active duty military members are not eligible for appointment unless currently on terminal leave. 4. SF-50: If applicable, all current and former Federal employees must submit a copy of your latest SF50 (Notification of Personnel Action) showing your tenure, grade and step, and type of position occupied (i.e., Excepted or Competitive); or similar Notification of Personnel Action documentation, i.e., Transcript of Service, Form 1150, etc. Failure to provide latest SF50 will result in you being rated ineligible for this position. If selected, additional documentation may be required prior to appointment.",
                            "Benefits": "",
                            "BenefitsUrl": "https://www.usajobs.gov/Help/working-in-government/benefits/",
                            "BenefitsDisplayDefaultText": True,
                            "OtherInformation": "DCSA, as a newly designated Defense Agency is undergoing a multi-year transformation that includes a significant expansion of predecessor agencies' authorities and responsibilities. Mission accretion and associated growth in personnel and resources requires deliberate coordination and planning across operations and support activities to achieve effective outcomes while simultaneously establishing and integrating new activities, initiatives and projects. The new organization will be comprised of nearly 13,000 government and contractor personnel operation throughout the United States and overseas supporting stakeholders across the federal government. VETERANS PREFERENCE/CURRENT OR FORMER FEDERAL\nIn accordance with DoD Instruction 1400.25, Volume 2005, veterans preference is not required to be applied when considering candidates with prior Federal competitive or excepted service who have completed a probationary or trial period and have not been separated for cause. Therefore, veterans preference will not be applied to applicants with current federal service, or former federal civilian service meeting the above criteria. COVID19 - To ensure compliance with an applicable preliminary nationwide injunction, which may be supplemented, modified, or vacated, depending on the course of ongoing litigation, the Federal Government will take no action to implement or enforce the COVID-19 vaccination requirement pursuant to Executive Order 14043 on Requiring Coronavirus Disease 2019 Vaccination for Federal Employees. Federal agencies may request information regarding the vaccination status of selected applicants for the purposes of implementing other workplace safety protocols, such as protocols related to masking, physical distancing, testing, travel, and quarantine. Other Notes: Re-employed Annuitant: This position does not meet criteria for re-employed annuitant. The DoD criteria for hiring Re-employed Annuitants can be found at: https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/140025/1400.25-V300.pdf Applicants selected from this announcement may be required to serve a two-year trial period. If selected, Federal employees currently serving in the competitive service must acknowledge that they will voluntarily leave the competitive service by accepting an offer of employment for a DCIPS excepted service positions. If selected, non-DCIPS candidates must acknowledge in writing that the position they have been selected for is in the excepted service and covered by DCIPS. Selection under this appointment authority does not confer civil service competitive status. All current and former Federal employees must submit a copy of your latest SF50 (Notification of Personnel Action) showing your tenure, grade and step, and type of position occupied (i.e., Excepted or Competitive); or similar Notification of Personnel Action documentation, i.e., Transcript of Service, Form 1150, etc.",
                            "KeyRequirements": [],
                            "WithinArea": "False",
                            "CommuteDistance": "0",
                            "ServiceType": "02",
                            "AnnouncementClosingType": "01",
                            "AgencyContactEmail": "DHRS-DDCSA@dla.mil",
                            "AgencyContactPhone": "614-692-2886",
                            "SecurityClearance": "Sensitive Compartmented Information",
                            "DrugTestRequired": "True",
                            "PositionSensitivitiy": "Special-Sensitive (SS)/High Risk",
                            "AdjudicationType": [
                                "Suitability/Fitness"
                            ],
                            "TeleworkEligible": True,
                            "RemoteIndicator": False
                        },
                        "IsRadialSearch": False
                    }
                },
                "RelevanceRank": 0
            },
            {
                "MatchedObjectId": "645856400",
                "MatchedObjectDescriptor": {
                    "PositionID": "22-NA-IM-02231-11441899-GOV",
                    "PositionTitle": "Data Scientist",
                    "PositionURI": "https://www.usajobs.gov:443/GetJob/ViewDetails/645856400",
                    "ApplyURI": [
                        "https://www.usajobs.gov:443/GetJob/ViewDetails/645856400?PostingChannelID="
                    ],
                    "PositionLocationDisplay": "Multiple Locations",
                    "PositionLocation": [
                        {
                            "LocationName": "Washington, District of Columbia",
                            "CountryCode": "United States",
                            "CountrySubDivisionCode": "District of Columbia",
                            "CityName": "Washington, District of Columbia",
                            "Longitude": -77.032,
                            "Latitude": 38.8904
                        },
                        {
                            "LocationName": "Las Vegas, Nevada",
                            "CountryCode": "United States",
                            "CountrySubDivisionCode": "Nevada",
                            "CityName": "Las Vegas, Nevada",
                            "Longitude": -115.14,
                            "Latitude": 36.1719
                        }
                    ],
                    "OrganizationName": "National Nuclear Security Administration",
                    "DepartmentName": "Department of Energy",
                    "JobCategory": [
                        {
                            "Name": "Data Science Series",
                            "Code": "1560"
                        }
                    ],
                    "JobGrade": [
                        {
                            "Code": "NQ"
                        }
                    ],
                    "PositionSchedule": [
                        {
                            "Name": "Full-time",
                            "Code": "1"
                        }
                    ],
                    "PositionOfferingType": [
                        {
                            "Name": "Permanent",
                            "Code": "15317"
                        }
                    ],
                    "QualificationSummary": "SPECIALIZED EXPERIENCE REQUIREMENTS A qualified candidate's online application and resume must demonstrate at least one year of specialized experience equivalent to the next lower NNSA Demonstration Project pay band or GS grade level in the Federal service, i.e., NQ-03 or GS-14. Specialized experience for this position is defined as: 1. Experience gathering and analyzing data using statistical software (including either Python or R) as part of data analysis to answer questions (not including for automation purposes); writing analysis solutions that are programmatic and repeatable. 2. Experience performing research and preparing materials for publication or presentation such as reports, research articles, source code, or other published content.\n3. Experience developing, deploying, and explaining machine learning and traditional statistical models. 4. Experience organizing and analyzing large amounts of structured and unstructured data sets using data analytical tools; creating and implementing data collection and analysis tools while utilizing programming languages and environments such as, R, Python, SQL, Scala, Java, C/C++, Julia. \"Experience\" refers to paid and unpaid experience. Examples of qualifying unpaid experience may include: volunteer work done through National Service programs (such as Peace Corps and AmeriCorps); as well as work for other community-based philanthropic and social organizations. Volunteer work helps build critical competencies, knowledge, and skills; and can provide valuable training and experience that translates directly to paid employment. You will receive credit for all qualifying experience, including volunteer experience. CTAP/ICTAP candidates: To be considered \"well qualified\" you must meet all of the requirements as described in this section. If you are eligible for career transition assistance plans such as ICTAP or CTAP, you must meet the definition of \"well qualified\" which is defined as having a score of 85 or better. You must meet all qualifications and eligibility requirements within 30 days of the closing date of this announcement.",
                    "PositionRemuneration": [
                        {
                            "MinimumRange": "126233.0",
                            "MaximumRange": "176300.0",
                            "RateIntervalCode": "Per Year"
                        }
                    ],
                    "PositionStartDate": "2022-03-30T00:00:00.0000",
                    "PositionEndDate": "2022-04-18T23:59:59.9970",
                    "PublicationStartDate": "2022-03-30T00:00:00.0000",
                    "ApplicationCloseDate": "2022-04-18T23:59:59.9970",
                    "PositionFormattedDescription": [
                        {
                            "Label": "Dynamic Teaser",
                            "LabelDescription": "Hit highlighting for keyword searches."
                        }
                    ],
                    "UserArea": {
                        "Details": {
                            "JobSummary": "A successful candidate in this position will serve as a Data Scientist responsible for Designing data modeling processes, create algorithms and predictive models to extract data the OCIO needs, and performs custom analysis. Washington D.C. Locality Salary: Min: $126, 233.00 to $176,300.00 Las Vegas, NV Locality Salary: Min $113,488.00 to $173,540.00",
                            "WhoMayApply": {
                                "Name": "",
                                "Code": ""
                            },
                            "LowGrade": "4",
                            "HighGrade": "4",
                            "PromotionPotential": "4",
                            "OrganizationCodes": "DN/DNNN",
                            "Relocation": "False",
                            "HiringPath": [
                                "fed-transition",
                                "fed-competitive",
                                "vet"
                            ],
                            "TotalOpenings": "2",
                            "AgencyMarketingStatement": "Would you like to play a key role in a critical mission? If so, then the National Nuclear Security Administration (NNSA), Office of Mission Integration has the perfect employment opportunity for an Data Scientist. In this position you'll play an important role in accomplishing the national security mission of the Department of Energy's National Nuclear Security Administration. You will utilize your expertise to plan and conduct critical research and development directly supporting data governance across the Office of the Chief Information Officer (OCIO) and the agency.",
                            "TravelCode": "2",
                            "ApplyOnlineUrl": "https://apply.usastaffing.gov/Application/Apply",
                            "DetailStatusUrl": "https://apply.usastaffing.gov/Application/ApplicationStatus",
                            "MajorDuties": [
                                "As a Data Scientist, you will: Develop computational algorithms and statistical methods that find patterns and relationships in large volumes of data sourced from advanced hardware and software. Evaluate agency wide systems across highly diversified functional areas including but not limited to physical, IT cyber, and extrapolate concise use-cases from vaguely worded mission requirements. Direct the application of ML/AI across the areas of operational and Information Technology systems, system of systems, or architectures, which employ data sciences methodologies. Design data modeling processes, create algorithms and predictive models to extract data the OCIO needs, and performs custom analysis to manipulate large data sets and use them to identify trends and reach meaningful conclusions to inform OCIO strategic decisions."
                            ],
                            "Education": "This position has a positive education requirement. A. Degree: Mathematics, statistics, computer science, data science or field directly related to the position. The degree must be in a major field of study (at least at the baccalaureate level) that is appropriate for the position. OR B. Combination of education and experience: Courses equivalent to a major field of study (30 semester hours) as shown in paragraph A above, plus additional education or appropriate experience. Education must be obtained from an accredited institution recognized by the U.S. Department of Education. Applicants who have completed part or all of their education outside of the U.S. must have their foreign education evaluated by an accredited organization to ensure that the foreign education is comparable to education received in accredited educational institutions in the U.S. A written evaluation of any foreign education must be provided with your application in response to this vacancy announcement or be received by the closing date of this announcement. Failure to provide this evaluation will result in you being found unqualified for the position. For special instructions pertaining to foreign education, see the Department of Education website, and for a list of organizations that can evaluate foreign education, visit The National Association of Credential Evaluation Services. Education must be accredited by an accrediting institution recognized by the U.S. Department of Education in order for it to be credited towards qualifications. Therefore, provide only the attendance and/or degrees from schools accredited by accrediting institutions recognized by the U.S. Department of Education. **FOREIGN EDUCATION: Applicants who have completed part or all of their education outside of the U.S. must have their foreign education evaluated by an accredited organization to ensure that the foreign education is comparable to education received in accredited educational institutions in the U.S. A written evaluation of any foreign education must be provided with your application in response to this vacancy announcement or be received by the closing date of this announcement. Failure to provide this evaluation will result in you being found unqualified for the position. For special instructions pertaining to foreign education, see the Department of Education website, and for a list of organizations that can evaluate foreign education, visit The National Association of Credential Evaluation Services. Please Note: If your foreign education has already been accepted by an accredited U.S. educational institution as part of a degree program with that institution, you do not need to provide an evaluation of foreign education but must submit a copy of the transcripts listing the degree from the U.S. accredited institution that accepted your foreign education. Failure to provide all of the required information as stated in this vacancy announcement may result in an ineligible rating or may affect the overall rating.",
                            "Requirements": "Subject to Random Drug Testing Must pass a pre-employment drug test. Favorable suitability determination required. Financial Disclosure is required. Must be able to obtain/maintain a Q level Security Clearance. You must be a United States Citizen. This employer participates in the e-Verify program. Males must abide by Selective Service registration requirements. Compliance with Homeland Security Presidential Directive (HSPD-12) governing personal identity which will require that you provide two forms of identification. To ensure compliance with an applicable preliminary nationwide injunction, which may be supplemented, modified, or vacated, depending on the course of ongoing litigation, the Federal Government will take no action to implement or enforce the COVID-19 vaccination requirement pursuant to Executive Order 14043 on Requiring Coronavirus Disease 2019 Vaccination for Federal Employees. Therefore, to the extent a Federal job announcement includes the requirement that applicants must be fully vaccinated against COVID-19 pursuant to E.O. 14043, that requirement does not currently apply. Federal agencies may request information regarding the vaccination status of selected applicants for the purposes of implementing other workplace safety protocols, such as protocols related to masking, physical distancing, testing, travel, and quarantine. A one year probationary period may be required.",
                            "Evaluations": "The Department of Energy uses an application tracking system to evaluate the responses you provide in the applicant assessment questionnaire to determine if you meet the minimum qualifications necessary for this position. Then, the HR Office and/or Subject Matter Expert (SME) will conduct a quality review of your application and supporting documentation to determine if your qualifications meet the criteria for referral to the selecting official. Merit Promotion & VEOA Procedures: If you are minimally qualified for this job, your responses to the self-assessment questions (True/False, Yes/ No, Multiple Choice questions) will be evaluated to determine if you are a best qualified candidate. If you rate yourself higher than is supported by your application materials, your responses may be adjusted and/or you may be excluded from consideration for this job. Due weight will also be given to federal employees, when applicable, for performance appraisals and awards in accordance with 5 CFR &#167; 335.103(b)(3). Federal employees must meet time-in-grade requirements and current employees must have at least a fully successful or equivalent performance rating to receive consideration. Your qualifications will be evaluated on the following competencies (knowledge, skills, abilities, and other characteristics): 1. Data Management. 2. Data Systems. 3. Database Management Systems. 4. Oral Communications. Your application and resume shall demonstrate that you possess the following Competencies. Do not provide a separate narrative written statement. Rather, you must describe in your application how your past work experience demonstrates that you possess the Competencies identified below. Cite specific examples of employment or experience contained in your resume and describe how this experience has prepared you to successfully perform the duties of this position. DO NOT write \"see resume\" in your application. Non-competitive Procedures: If you are applying under a non-competitive or special hiring authority, you will still be required to answer the assessment questions. However, you will not be evaluated against the rating and ranking criteria. Your resume and supporting documentation will be used to determine if you are minimally qualified for this job. Veterans' Preference will be applied when required by the hiring authority (e.g., VRA, Schedule A). All qualified Non-competitive applicants and the best qualified Merit Promotion and VEOA applicants will be referred to the hiring manager for consideration. Career Transition Assistance Programs: To receive selection priority for this position, you must: 1) meet the eligibility criteria; and 2) be rated \"well-qualified\", which is defined as having a score of 85 or better. You must meet all qualifications and eligibility requirements by the closing date of this announcement. If your resume is incomplete or does not support the responses you provided in your online questionnaire, or if you fail to submit all required documentation before the vacancy closes, you may be rated 'ineligible', 'not qualified', or your score may be adjusted accordingly.",
                            "HowToApply": "Please read the entire announcement and all the instructions before you begin an application. To apply for this position, you must complete the initial online application, to include submission of the required documentation specified in the Required Documents section. A complete application package must be submitted by 11:59 PM (EST) on the announcement closing date to receive consideration. The application process is as follows: You must have a login.gov account to sign into USAJOBS: https://www.usajobs.gov/Help/how-to/account/. To begin the application process in USAJOBS, click the Apply Online button. Answer the questions presented in the application and attach all required and supporting documentation. You must click the Submit Application button prior to 11:59 pm (ET) on the announcement closing date. You may update your application, including supporting documentation, at any time during the announcement open period by returning to your USAJOBS account, select Update Application: https://my.usajobs.gov/Account/Login. This option will no longer be available once the announcement has closed. To verify the status of your application, during and after the announcement open period, log into your USAJOBS account; applications will appear on the Welcome screen. The Application Status will appear along with the date your application was last updated. For information on what each application status means, visit: https://www.usajobs.gov/Help/how-to/application/status/. If you need help with login.gov or USAJOBS (e.g., account access, Resume Builder) visit the USAJOBS Help Center: https://www.usajobs.gov/Help/ If you experience difficulty applying on USAJOBS, after clicking the Apply Online button, or you are experiencing a significant hardship hindering your ability to apply online, the Agency Contact listed in the announcement can assist you during normal business hours. If you receive any system error messages, take screenshots if possible, to aid technical support.",
                            "WhatToExpectNext": "Once your online application is submitted you will receive a confirmation notification by email. The status of your application will be updated in USAJOBS as it is evaluated. You can check the status by logging into USAJOBS. You may also sign up to receive automatic emails anytime the status of your application changes by logging into your USAJobs Account and editing the Notification Settings. You will be contacted directly if an interview is required.",
                            "RequiredDocuments": "To apply for this position, you MUST provide a complete application package which includes:\nALL APPLICANTS: You must submit a resume supporting your specialized experience and responses to the online questionnaire. Your resume shall list all work experience (paid and unpaid); you must list the full name and address of the each employer. For all types of work experience, you shall indicate the start and end dates (include month, day, and year); you must also list the average number of hours per week that you worked. For paid work experience, you shall indicate your starting salary for each position and the highest salary you earned (if different). Your resume should also include any education and training you have completed (list the program title, subject area, number of hours completed, and completion date). You may list all incentive awards on your resume. Most recent two performance appraisals. For more information about what to include in your resume, please view this USAJOBS Resume Tutorial video on YouTube. Most DOE offices will allow you to submit a resume in the format of your choice (as an attached document or as a USAJOBS Resume Builder format). However, some offices may require one specific format. You will be notified at the time you click 'Apply Online' which type of resume is acceptable. It is important that you are complete and thorough in your resume. If any of the above information is not included in your resume, we may not be able to fully credit you for your experience. Cover Letter, optional, expressing additional information not covered in your resume. Transcripts, if specific educational requirements are indicated in this job announcement. Unofficial transcripts or any report listing institution, course title, credits earned (semester or quarter hour) and final grade is acceptable. It is your responsibility to provide adequate proof that you meet the educational requirements. Submit one or more of the following to support your eligibility(s) to apply to this job announcement: SF-50, \"Notification of Personnel Action\" (current/former federal employees): To properly verify status eligibility, your SF-50 must show the following. If you do not submit an appropriate SF-50, we cannot verify your status eligibility! Full position title; appointment type; occupational series; pay plan, grade, and step; tenure code; and service computation date (SCD). If your current position SF50 does not indicate you have competitive service status or does not reflect the pay plan and grade of the highest position you have held in the competitive service, in addition to your current SF50, you must provide your previous SF-50s that provide the proof of competitive status and highest grade held on a permanent basis. If specific educational requirements are indicated for this vacancy: experience.\">Documentation verifying your educational claims which can include unofficial transcripts or any report listing institution, course title, credits earned and final grade. Please see the Education section for more information. Veterans: DD-214 Member Copy 4 showing type of discharge/character of service; current active duty members- certification of expected discharge or release from active duty under honorable conditions dated within 120 days; SF-15 Form and related documentation; VA letter. For more information visit the USAJOBS Help Center &amp; OPM CHCOC website for VOW information.\nIndividuals with Disabilities: Schedule A letter from a physician, local, state or federal rehabilitation office citing your eligibility under 5 CFR 213.3102 (u). For more information visit the USAJOBS Help Center. Certain Military Spouses: Permanent Change of Station (PCS) orders authorizing you to accompany the Military member to the new duty permanent station; OR verification of the member's 100% disability (VA Letter); and/or verification of the member's death while on active duty (DD-1300 and Death Certificate) AND verification of the marriage to the service member (i.e., a marriage license or other legal documentation verifying marriage). For more information visit the USAJOBS Help Center. Other non-competitive or special appointing authorities: provide documentation which supports your eligibility. Career Transition Assistance Program/Interagency Career Transition Assistance Program documentation, if applicable (e.g., Certification of Expected Separation, Reduction-In-Force Separation Notice, or Notice of Proposed Removal; SF-50 that documents the RIF separation action; and most recent performance appraisal.) For more information see the OPM Guide to Career Transition. Failure to submit any of the above mentioned required documents may result in loss of consideration due to an incomplete application package. It is your responsibility to ensure all required documents have been submitted.",
                            "Benefits": "",
                            "BenefitsUrl": "https://www.opm.gov/healthcare-insurance/healthcare/plan-information/summary-of-benefits",
                            "BenefitsDisplayDefaultText": True,
                            "OtherInformation": "The U.S. Department of Energy fosters a diverse and inclusive workplace and is an Equal Opportunity Employer. Veterans and persons with disabilities are encouraged to apply. For more information, please visit the links at the bottom of this page or visit the FedsHireVets website. If you believe that you are eligible for the Interagency Career Transition Assistance Program (ICTAP), please visit the OPM ICTAP/CTAP website for more information. In order to be considered under the ICTAP program, your application must score within the pre-established \"well qualified\" category as stated in the Qualifications section. More than one selection may be made from this vacancy announcement. Some positions may require completion of a probationary period of up to 1 (one) year. Many positions require successful completion of a background investigation. All males born after December 31,1959 must abide by laws regarding Selective Service registration. To learn more about this law, visit the Selective Service web page, Who Must Register. If you are not registered and don't have an approved exemption, you will not be eligible for employment with the Federal government. A Recruitment/Relocation Incentive may be authorized for a highly qualified applicant in accordance with Agency policy. EEO Policy: Click HERE.\nReasonable Accommodation Policy: Click HERE.\nVeterans Information: Click HERE.\nTelework: Click HERE.\nSelective Service Registration: Click HERE.\nInformation about the NNSA Demonstration project can be found by clicking HERE.",
                            "KeyRequirements": [],
                            "WithinArea": "False",
                            "CommuteDistance": "0",
                            "ServiceType": "01",
                            "AnnouncementClosingType": "01",
                            "AgencyContactEmail": "mary.steuck@nnsa.doe.gov",
                            "SecurityClearance": "Q Access Authorization",
                            "DrugTestRequired": "True",
                            "PositionSensitivitiy": "Critical-Sensitive (CS)/High Risk",
                            "AdjudicationType": [
                                "Credentialing",
                                "Suitability/Fitness",
                                "National security"
                            ],
                            "TeleworkEligible": True,
                            "RemoteIndicator": False
                        },
                        "IsRadialSearch": False
                    }
                },
                "RelevanceRank": 0
            }
        ],
        "UserArea": {
            "NumberOfPages": "1084",
            "IsRadialSearch": False
        }
    }
}


@pytest.fixture(scope="function")
def response_json():
    return api_response


@pytest.fixture(autouse=True)
def mock_constants(monkeypatch):
    monkeypatch.setattr("usagovjobs.main.constants.BASE_URL", "test-url-")
    monkeypatch.setattr(constants, name="USA_JOBS_API_KEY", value="test-key")
    monkeypatch.setattr(constants, name="USA_JOBS_USER_AGENT", value="test-user-agent")
    monkeypatch.setattr(constants, name="HOST", value="test-host")


@pytest.fixture(scope="function")
def headers():
    return {
        "Host": constants.HOST,
        "User-Agent": constants.USA_JOBS_USER_AGENT,
        "Authorization-Key": constants.USA_JOBS_API_KEY,
    }


@pytest.fixture(scope="function")
def mock_request_object(mock_response_object):
    class Mock_Requests:
        def get(self, url, headers, params):
            return mock_response_object

    return Mock_Requests()


@pytest.fixture(scope="function")
def mock_response_object():
    class Mock_Response:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def status(self):
            return self.status_code

    return Mock_Response(json_data={"test": "data"}, status_code=200)
