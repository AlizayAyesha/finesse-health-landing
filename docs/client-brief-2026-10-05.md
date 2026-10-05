# Finesse Health & Co. — Client Brief

**Date:** 5 October 2026  
**Project:** Rebuild static site under `/workspace/finesse-health/`  
**Do not:** deploy or push to GitHub

## CRITICAL POSITIONING

Finesse Health & Co. is an **International Dental Concierge & Patient Coordination Service** connecting Australian patients with accredited dental specialists in India.

It is **NOT** a healthcare provider, clinic, or hospital. Never imply clinical care is delivered by Finesse. Emphasize administrative/concierge facilitation only.

## Brand

- Navy: `#253350`
- Sage: `#90A28B`
- Warm off-white / paper: `#F4F0EA`
- Fonts: Montserrat (headings), Source Sans 3 (body)
- Keep existing logo assets in `assets/`

## Pages

1. `index.html` — landing page
2. `terms-and-disclaimer.html` — full legal copy (verbatim below)
3. `privacy.html` — Privacy Policy (APP-aligned draft matching contact details)

## Landing page structure

- **Header/nav:** logo, How It Works, Services Facilitated, About Us, Contact, primary CTA "Request an Initial Assessment"
- **Hero:** premium, calm aesthetic; headline about accessible premium dental transformations abroad (concierge framing)
- **How It Works (4 steps):**
  1. Submit Enquiry & Dental Records (secure share of records/OPG X-rays)
  2. Custom Clinic Treatment Plan (licensed specialist clinic in India reviews and issues individualized clinical quote)
  3. Travel & Concierge Coordination (itinerary, transfers, appointment schedules)
  4. Treatment & Return (care abroad with full administrative support)
- **Transparency banner (exact or very close):**
  > Finesse Health & Co. provides administrative, booking, and concierge facilitation. All clinical assessments, diagnoses, surgeries, and warranties are provided exclusively by treating dental clinics in India.
- **Services Facilitated:** e.g. Implants, Veneers, Full Mouth Rehabilitation, etc. — frame as "treatments we help you enquire about / coordinate", not "we perform"
- **About Us:** short concierge positioning
- **Lead Capture Form** (`#enquiry` / CTA anchors):
  - Fields: Full Name, Phone, Email, Preferred Dental Treatment (select: Implants, Veneers, Full Mouth Rehabilitation, Other), secure file-upload for dental X-rays/photos
  - Mandatory checkbox: "I have read and agree to the Terms of Service and acknowledge the Medical Disclaimer." linking to `terms-and-disclaimer.html`
  - Front-end only for now (success message; README notes backend wiring needed)
- **Footer contact:**
  - Address: Level 1, 93 George Street, Parramatta, NSW 2150 (Google Maps link)
  - Email: finessehealthandco@gmail.com.au
  - Phone: +61 448 415 873 (`tel:+61448415873`)
  - Links: Terms of Service & Medical Disclaimer | Privacy Policy | Contact Us

## Terms page — FULL LEGAL COPY (verbatim)

FINESSE HEALTH & CO. — TERMS OF SERVICE & MEDICAL DISCLAIMER  
Last Updated: October 2026  
Business Name: Finesse Health & Co.  
Principal Place of Business: Level 1, 93 George Street, Parramatta, NSW 2150, Australia  
Contact: finessehealthandco@gmail.com.au | +61 448 415 873

IMPORTANT NOTICE: PLEASE READ CAREFULLY  
By accessing this website, submitting an inquiry, transmitting medical or dental records, or engaging the services of Finesse Health & Co. ("the Company", "we", "us", or "our"), you ("the Client", "Patient", or "User") agree to be legally bound by these Terms of Service and Medical Disclaimer. If you do not agree to these terms, you must not use this website or our coordination services.

### 1. NATURE OF SERVICES — INTERMEDIARY FACILITATOR ONLY

1.1. Non-Clinical Status: Finesse Health & Co. is an independent booking, logistics, and patient coordination facilitator. Finesse Health & Co. is NOT a medical, dental, or healthcare provider, clinic, or hospital.

1.2. No Doctor-Patient Relationship: No content, interaction, or communication (written, oral, or electronic) provided by Finesse Health & Co., its owners, contractors, patient coordinators, or affiliates shall be construed as establishing a doctor-patient, dentist-patient, or healthcare practitioner-patient relationship.

1.3. Independent Third Parties: All medical, dental, surgical, cosmetic, and diagnostic procedures are performed entirely by independent, autonomous third-party clinics, hospitals, and licensed practitioners located overseas (including, but not limited to, the Republic of India). These providers are independent contractors and are not employees, partners, agents, or joint-venturers of Finesse Health & Co.

### 2. MEDICAL & CLINICAL DISCLAIMER

2.1. Informational Content Only: All materials, articles, procedural descriptions, FAQs, case studies, images, and pricing guides displayed on this website are provided strictly for general educational and informational purposes. Nothing on this website constitutes professional medical or dental diagnosis, prognosis, advice, or treatment planning.

2.2. Inherent Surgical Risks: Any elective, medical, or dental surgical procedure carries inherent clinical, biological, and anaesthetic risks, including but not limited to infection, nerve damage, aesthetic dissatisfaction, structural failure (e.g., implant or crown failure), prolonged pain, and post-operative complications. Outcomes vary significantly between individuals.

2.3. Independent Evaluation Required: Prior to traveling abroad or undertaking any clinical procedure, Clients are strongly advised to consult an independent Australian registered general practitioner (GP) and/or registered Australian dental practitioner (AHPRA-registered) to evaluate their general health, dental suitability, and travel fitness.

2.4. No Warranties or Guarantees: Finesse Health & Co. makes no representations, warranties, or guarantees—express or implied—regarding the success, durability, permanence, or outcome of any clinical treatment performed overseas. Under no circumstances does Finesse Health & Co. guarantee "painless," "100% successful," or "risk-free" procedures.

### 3. ROLE OF PATIENT COORDINATORS & SUBCONTRACTORS

3.1. Strictly Administrative Scope: International Patient Coordinators and representatives working with or on behalf of Finesse Health & Co. operate strictly as administrative, scheduling, translation, and concierge liaisons.

3.2. No Clinical Advice from Staff: Patient Coordinators are legally prohibited from providing clinical opinions, interpreting X-rays/radiographs, recommending specific surgical techniques, or determining medical suitability. Any preliminary quotes or treatment overviews provided by a Coordinator are merely verbatim or synthesized transmissions of recommendations issued directly by the overseas treating clinic.

3.3. Direct Clinical Relationship: Any diagnosis, treatment plan, procedural warranty, or informed consent is entered into directly and exclusively between the Client and the overseas treating dental clinic.

### 4. PATIENT RECORDS & PRIVACY (SENSITIVE HEALTH DATA)

4.1. Consent to Disclose Overseas: By uploading or sending dental charts, OPG X-rays, medical histories, or clinical photographs through our website or communication channels, the Client explicitly consents to Finesse Health & Co. securely transmitting this sensitive health data to accredited third-party dental practitioners and clinical coordinators located overseas (primarily India) solely for assessment, triage, and quotation.

4.2. Accuracy of Information: The Client warrants that all medical, dental, and personal health disclosures provided are true, accurate, complete, and up to date. Finesse Health & Co. bears no responsibility for compromised clinical plans resulting from undisclosed health conditions, medications, or inaccurate dental records.

4.3. Privacy Compliance: In accordance with the Privacy Act 1988 (Cth) and the Australian Privacy Principles (APPs), we maintain reasonable security measures to protect your personal and health information from unauthorized access, loss, or misuse.

### 5. FINANCIAL TERMS & PAYMENT BOUNDARIES

5.1. Facilitation vs. Clinical Fees: Any administrative, concierge, or booking coordination fees charged by Finesse Health & Co. cover administrative, logistics, customer service, and scheduling facilitation only.

5.2. Clinical Treatment Payments: Payments for clinical consultations, diagnostics, dental materials, surgeries, laboratory fees, and hospital admissions are payable either directly to the overseas healthcare facility or held on designated client account for direct remittance to the clinical provider, as stipulated in individual booking schedules.

5.3. Treatment Plan Variations: Preliminary quotes provided before travel are estimates based on supplied photographic/radiographic records. The treating dentist overseas reserves the clinical right to modify, add, or alter proposed treatments following a direct, in-person clinical examination and three-dimensional imaging (CBCT). Any resulting price adjustments are strictly between the Client and the treating clinic.

### 6. TRAVEL, FLIGHTS, AND CROSS-BORDER LOGISTICS

6.1. Travel Bookings: Unless explicitly bundled via an accredited travel agency partner, Clients are solely responsible for booking their own international flights, obtaining appropriate visas, and ensuring valid passport validity (minimum 6 months validity required).

6.2. Fitness to Fly & Medical Clearances: Clients are solely responsible for obtaining medical clearance to travel post-surgery. Finesse Health & Co. accepts no liability for airline cancellations, missed flights, border entry refusals, quarantine requirements, or medical emergencies occurring in transit.

6.3. Medical Travel Insurance Requirement: Standard Australian travel insurance policies explicitly exclude elective overseas dental and medical complications. Clients are strongly advised to obtain specialized medical tourism insurance (e.g., Medical Travel Shield) that specifically covers elective dental procedures, surgical complications, emergency revisions, and travel extensions.

### 7. LIMITATION OF LIABILITY & INDEMNITY

7.1. Exclusion of Clinical Negligence: To the maximum extent permitted by the Competition and Consumer Act 2010 (Cth) (Australian Consumer Law): Finesse Health & Co., its directors, officers, employees, independent contractors, and coordinators shall not be liable for any direct, indirect, incidental, punitive, special, or consequential loss, injury, illness, physical disfigurement, disability, clinical negligence, malpractice, or death resulting from any treatment, advice, or omissions of overseas clinics, dentists, oral surgeons, or hospitals.

7.2. Limitation of Facilitation Liability: Where liability cannot be excluded by law, Finesse Health & Co.'s maximum aggregate liability to the Client arising out of or related to our facilitation services (whether in contract, tort, or statute) is strictly limited to the total facilitation fee paid by the Client to Finesse Health & Co. for the specific coordination service in dispute.

7.3. Indemnity: The Client agrees to defend, indemnify, and hold harmless Finesse Health & Co., its coordinators, agents, and affiliates against any claims, liabilities, damages, losses, or legal costs arising from: (1) The Client's breach of these Terms; (2) Any misrepresentation or omission of medical history by the Client; (3) Any clinical dispute, claim, or malpractice action initiated by the Client against an overseas dental clinic.

### 8. COMPLAINTS, REVISIONS & AFTERCARE

8.1. Overseas Dispute Jurisdiction: Any clinical grievance, allegation of negligence, malpractice claim, or dispute regarding dental artistry, functionality, or clinical outcomes must be resolved directly with the treating dental clinic in India in accordance with the laws and medical dispute mechanisms of the local jurisdiction where the procedure occurred.

8.2. Local Follow-Up in Australia: Finesse Health & Co. does not provide routine post-operative care, suture removal, emergency clinical aftercare, or local dental management in Australia. Clients must arrange routine preventive maintenance and ongoing hygiene with an Australian dental practitioner upon return.

### 9. GOVERNING LAW & JURISDICTION

These Terms of Service and any administrative coordination agreement entered into with Finesse Health & Co. are governed by and construed in accordance with the laws of New South Wales, Australia. The parties submit to the exclusive jurisdiction of the courts of New South Wales and the Commonwealth of Australia for the resolution of any disputes regarding administrative facilitation services.

### 10. CLIENT ACKNOWLEDGEMENT & ACCEPTANCE

By ticking the confirmation box on our enquiry forms or paying an administrative deposit, you confirm that: (1) You have read, understood, and agreed to this entire Terms of Service & Medical Disclaimer; (2) You acknowledge that Finesse Health & Co. is purely a travel and patient coordination facilitator; (3) You freely and voluntarily assume all clinical, financial, and travel risks associated with undergoing elective dental treatment abroad.

## Design notes

- Mobile-first, accessible, meta/OG tags, favicons from `assets/`
- Update any old GP clinic copy, fake Sydney CBD hours, old phone/email/address
- Screenshots: mobile-390 and desktop-1440 of home + terms under `screenshots/`
