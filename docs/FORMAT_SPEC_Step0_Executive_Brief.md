# Step 0: Executive Brief Extraction - Output Format Specification

**Version**: 1.0
**Purpose**: Exact format specification for Step 0 outputs to ensure consistency and professional quality across all Executive Brief extractions
**Document Type**: Primary intake document for VIANEO 8-Step Evaluation System
**Last Updated**: 2025-11-21

---

## Overview

The Executive Brief is the foundational document of the VIANEO framework. It distills complex innovation proposals into a standardized, evidence-backed summary that enables rapid assessment and consistent evaluation. This specification defines the exact format, content requirements, and quality standards for all Step 0 outputs.

**Critical Success Factors:**
- Strict adherence to character limits (enforces clarity)
- Solution-neutral problem statements (prevents solution bias)
- Evidence-based claims (all assertions must be quantified)
- Maturity-appropriate expectations (aligns validation depth with stage)

---

## Required Output Structure

### Document Header (Required)

```markdown
# Executive Brief Template

## Project Information
**Project Name:** [Enter project name]
**Date Prepared:** YYYY-MM-DD
**Prepared By:** [Name or Assessment Team]
**Executive Brief ID:** EB-YYYY-NNN

---
```

**Critical Formatting Rules:**

1. **Title**: Must be exactly "# Executive Brief Template" (H1 level)
2. **Section**: "## Project Information" (H2 level)
3. **Date Format**: YYYY-MM-DD (ISO 8601 standard, e.g., 2025-01-15)
4. **Brief ID Format**: EB-YYYY-NNN where:
   - YYYY = Four-digit year
   - NNN = Three-digit sequential number (001, 002, etc.)
   - Example: EB-2025-001
5. **Separator**: Three dashes (---) after header

**Common Errors to Avoid:**
- ❌ Date format MM/DD/YYYY or DD-MM-YYYY
- ❌ Brief ID without leading zeros (EB-2025-1)
- ❌ Missing horizontal rule separator
- ❌ Using wrong header levels (H3 instead of H2)

---

## SECTION B1: Project Name and One-Line Description

### Exact Format:

```markdown
## Section B1: Project Name and Tagline
**Character Limit:** 150 characters maximum

**Project Name:**
[Enter official project name]

**One-Line Tagline:**
[Concise description capturing the essence of the project]

**Quality Checklist:**
- [ ] Name is clear and memorable
- [ ] Tagline is under 150 characters
- [ ] Tagline captures core value proposition

---
```

### Content Requirements:

**Project Name:**
- Official, legal name of the project/business
- Avoid generic descriptors ("The Company", "Our Solution")
- Use title case formatting
- Maximum 50 characters recommended
- Must be consistent across all documents

**One-Line Tagline:**
- TOTAL of project name + tagline must be ≤ 150 characters (including spaces)
- Must communicate WHAT the solution does and FOR WHOM
- Must be jargon-free and understandable to non-experts
- Should differentiate from obvious alternatives
- NO marketing hyperbole ("revolutionary", "game-changing")

**Examples:**

✅ **Good:**
- Project Name: "MediTrack"
- Tagline: "AI-powered medication adherence monitoring for elderly patients with chronic conditions"
- Total: 90 characters

✅ **Good:**
- Project Name: "EduLearn"
- Tagline: "Adaptive tutoring platform helping K-12 students master math through personalized AI guidance"
- Total: 97 characters

❌ **Bad:**
- Project Name: "Revolutionary Health Solutions Inc."
- Tagline: "Transforming healthcare through cutting-edge innovation"
- Problems: Generic, no specifics, marketing language, doesn't explain what/who

❌ **Bad:**
- Tagline: "We leverage machine learning algorithms to create synergistic value propositions"
- Problems: Jargon-heavy, vague, no clear beneficiary

### Validation Rules:

1. **Character Count**: Combined name + tagline ≤ 150 characters
2. **Clarity Test**: Non-expert can understand what and who in 5 seconds
3. **Specificity Test**: Contains at least one concrete noun (medication, students, farmers)
4. **Differentiation Test**: Not interchangeable with 5+ other companies
5. **Completeness Test**: Answers "What does it do?" and "Who is it for?"

---

## SECTION B2: Problem Statement

### Exact Format:

```markdown
## Section B2: Problem Statement
**Character Limit:** 300 characters maximum

**Problem Description:**
[Describe the problem in solution-neutral terms]

**Problem Characteristics:**
- **Severity:** [1-5 scale]
- **Frequency:** [How often does this problem occur?]
- **Affected Population:** [Size and description]

**Quality Checklist:**
- [ ] Problem is stated without reference to solution
- [ ] Problem statement is under 300 characters
- [ ] Severity and frequency are quantified
- [ ] Affected population is specified

---
```

### Content Requirements:

**Problem Description (300 characters max):**
- Must be **solution-neutral** (no mention of apps, platforms, AI, etc.)
- Must quantify impact (time lost, money wasted, lives affected)
- Must specify WHO experiences the problem
- Should include current alternative/workaround if applicable
- Must avoid solution language ("lack of X solution", "no platform exists")

**Problem Characteristics:**

**Severity (1-5 scale):**
- 1 = Minor inconvenience, low impact
- 2 = Moderate annoyance, some cost/time waste
- 3 = Significant pain point, measurable negative impact
- 4 = Major problem, substantial financial/health/safety impact
- 5 = Critical/life-threatening, catastrophic consequences

**Frequency:**
- Use specific timeframes: "Daily", "2-3x per week", "Monthly", "Annually"
- Include prevalence: "Affects 60% of target population daily"
- Quantify: "Occurs 15 times per patient per month"

**Affected Population:**
- Must include SIZE: "2.5M elderly Americans", "15K hospital administrators"
- Must include DESCRIPTION: Demographics, location, industry
- Should specify PRIMARY vs SECONDARY affected groups

**Examples:**

✅ **Good (295 characters):**
"Elderly patients with 5+ chronic conditions forget medication doses 40% of the time, leading to 125K hospitalizations annually in the US. Current paper logs are lost or filled incorrectly. Family caregivers lack visibility into adherence, discovering problems only during crises."

Characteristics:
- Severity: 5 (life-threatening)
- Frequency: Daily (40% of doses)
- Affected Population: 8M elderly Americans with multiple chronic conditions

✅ **Good (287 characters):**
"Middle school math teachers spend 12 hours weekly grading assignments and identifying individual learning gaps. Class sizes of 30+ make personalized intervention impossible. Students fall behind without targeted support, creating compounding knowledge gaps that persist into high school."

Characteristics:
- Severity: 4 (educational impact)
- Frequency: 12 hours per teacher per week
- Affected Population: 150K middle school math teachers, 4.5M students

❌ **Bad:**
"Patients need better medication tracking tools. There's no good app for this problem."
- Problems: Solution language ("app"), not quantified, no affected population size

❌ **Bad:**
"The healthcare industry faces numerous challenges in medication management across various demographics."
- Problems: Too vague, no specifics, no quantification, no severity indication

### Validation Rules:

1. **Solution Neutrality Test**: Can you describe the problem without using words like: app, platform, software, AI, tool, system, solution, service
2. **Quantification Test**: Contains at least 2 numerical values (%, count, time, money)
3. **Impact Test**: Clear consequence stated (hospitalizations, time waste, revenue loss)
4. **Character Limit**: Exactly ≤ 300 characters
5. **Severity Justification**: Severity rating matches problem description
6. **Population Sizing**: Affected population includes a number with unit (M, K, thousands)

---

## SECTION B3: Proposed Solution

### Exact Format:

```markdown
## Section B3: Solution Overview
**Character Limit:** 300 characters maximum

**Solution Description:**
[Describe what the solution does and how it addresses the problem]

**Solution Type:**
- [ ] Product
- [ ] Service
- [ ] Platform
- [ ] Other: [Specify]

**Key Features:**
1. [Feature 1]
2. [Feature 2]
3. [Feature 3]

**Quality Checklist:**
- [ ] Solution description is under 300 characters
- [ ] Clear connection to problem statement
- [ ] Key features are listed
- [ ] Solution type is identified

---
```

### Content Requirements:

**Solution Description (300 characters max):**
- Must explain WHAT the solution does (functionality)
- Must explain HOW it addresses the specific problem from B2
- Should include primary mechanism/approach
- Must avoid marketing language
- Should specify form factor if relevant (mobile app, web platform, physical device)

**Solution Type:**
- **Product**: Tangible deliverable (software, hardware, physical good)
- **Service**: Human-delivered ongoing support (consulting, managed service)
- **Platform**: Connects multiple parties (marketplace, network)
- **Other**: Hybrid or novel format (specify clearly)

**Key Features:**
- List 3-5 PRIMARY features (not exhaustive list)
- Each feature should be 5-10 words
- Features should map to problem characteristics from B2
- Focus on WHAT not HOW (user-facing, not technical)
- Use action verbs: "Sends daily reminders", "Tracks completion", "Generates reports"

**Examples:**

✅ **Good (298 characters):**
"Mobile app that sends personalized medication reminders based on prescriptions, tracks dose completion via photo confirmation, and alerts family caregivers when doses are missed. Uses simple tap-based interface designed for limited tech literacy. Syncs with pharmacies for automated updates."

Solution Type: Product (Mobile Application)

Key Features:
1. Personalized medication reminders synced to prescription schedules
2. Photo-based dose verification and completion tracking
3. Real-time caregiver alerts for missed medications
4. Pharmacy integration for automated prescription updates
5. Simple tap-based interface for elderly users

✅ **Good (286 characters):**
"AI-powered tutoring platform that auto-grades math assignments, identifies individual learning gaps, and generates personalized practice problems. Teachers receive class-level analytics dashboards. Students access adaptive problem sets that target their specific misconceptions."

Solution Type: Platform (EdTech SaaS)

Key Features:
1. Automated assignment grading with detailed error analysis
2. AI-generated personalized practice problem sets
3. Teacher analytics dashboard showing class-wide patterns
4. Student progress tracking and mastery indicators

❌ **Bad:**
"Our innovative solution leverages cutting-edge AI and machine learning to revolutionize medication adherence through a synergistic mobile-first approach."
- Problems: Marketing jargon, no specifics, doesn't explain what it actually does

❌ **Bad:**
"An app for medication tracking."
- Problems: Too vague, no detail on how it works, no differentiation

### Validation Rules:

1. **Character Limit**: Exactly ≤ 300 characters
2. **Problem Mapping**: Each key feature should address a specific aspect of the B2 problem
3. **Specificity Test**: Non-expert can visualize using the solution
4. **Differentiation Test**: Not generic (distinguishable from obvious alternatives)
5. **Jargon Check**: No more than 1 technical term (must be essential, not decorative)
6. **Feature Count**: 3-5 features listed (not 1-2, not 10+)

---

## SECTION B4: Target Market and Users

### Exact Format:

```markdown
## Section B4: Market and Users
**Character Limit:** 300 characters maximum

**Target Market:**
[Describe the target market]

**User/Buyer Distinction:**
- **Primary Users:** [Who uses the solution?]
- **Primary Buyers:** [Who pays for the solution?]
- **Are users and buyers the same?** [ ] Yes [ ] No

**Market Sizing:**
- **TAM (Total Addressable Market):** [Size]
- **SAM (Serviceable Addressable Market):** [Size]
- **SOM (Serviceable Obtainable Market):** [Size]

**Sizing Method:**
- [ ] Top-down
- [ ] Bottom-up
- [ ] Value theory

**Quality Checklist:**
- [ ] Market description is under 300 characters
- [ ] User/buyer distinction is clear
- [ ] Market sizes are quantified
- [ ] Sizing methodology is documented

---
```

### Content Requirements:

**Target Market Description (300 characters max):**
- Must specify PRIMARY target segment (not "everyone")
- Should include demographics: age, location, industry, role
- Should include psychographics: behaviors, needs, current solutions
- Must quantify market size with credible numbers
- Should note if B2B, B2C, or B2B2C model

**User/Buyer Distinction:**

Critical for pricing, distribution, and go-to-market strategy.

**When Users = Buyers** (e.g., B2C SaaS):
- Primary Users: Individual consumers who pay directly
- Primary Buyers: Same as users
- Example: Freelancers subscribing to productivity software

**When Users ≠ Buyers** (e.g., B2B, education, healthcare):
- Primary Users: People who interact with solution daily
- Primary Buyers: Decision-makers who control budget
- Example:
  - Users: Teachers and students
  - Buyers: School district administrators

**Market Sizing (TAM/SAM/SOM):**

**TAM (Total Addressable Market):**
- Global maximum if every potential customer bought
- Usually too large to be actionable
- Example: "$50B global EdTech market"

**SAM (Serviceable Addressable Market):**
- Portion of TAM you can reach with your business model
- Constrained by geography, regulations, channels
- Example: "$8B US K-12 math tutoring market"

**SOM (Serviceable Obtainable Market):**
- Realistic market share in 3-5 years
- Usually 1-10% of SAM for early-stage
- Example: "$80M (1% of SAM in Year 3)"

**Sizing Methodology:**

**Top-down:**
- Start with macro data (industry reports, government stats)
- Apply filters (geography, segment)
- Fastest but least precise
- Example: "15M elderly Americans × $500/year = $7.5B TAM"

**Bottom-up:**
- Start with unit economics
- Multiply by addressable customer count
- More credible for investors
- Example: "2,500 hospitals × 300 patients/hospital × $100/patient/year = $75M SAM"

**Value theory:**
- Calculate value created for customer
- Estimate willingness-to-pay based on value
- Best for novel categories
- Example: "Save 10 hours/week × $50/hour × 150K teachers = $3.9B annual value creation"

**Examples:**

✅ **Good (299 characters):**
"Primary target: US hospitals with 200+ beds (2,500 facilities) serving elderly patients with chronic conditions. Secondary: Home health agencies, assisted living. Users (nurses, patients) differ from buyers (hospital administrators). Initial focus: 100 hospitals in Northeast region."

User/Buyer Distinction:
- Primary Users: Nurses (dose administration), elderly patients (compliance)
- Primary Buyers: Hospital IT directors, Chief Medical Officers
- Are users and buyers the same? NO

Market Sizing:
- TAM: $12B (global medication adherence market)
- SAM: $3B (US hospitals 200+ beds)
- SOM: $90M (3% of SAM by Year 3)

Sizing Method: Bottom-up (2,500 hospitals × 300 patients avg × $400/patient/year)

✅ **Good (287 characters):**
"K-12 math teachers in US public schools (180K teachers) serving 5M middle school students. Teachers use platform for grading/analytics; students use for practice. School districts purchase (13K district buyers). Initial beachhead: 500 teachers in 5 urban districts (TX, CA, NY)."

User/Buyer Distinction:
- Primary Users: Math teachers (assessment), middle school students (practice)
- Primary Buyers: District curriculum directors, principals
- Are users and buyers the same? NO

Market Sizing:
- TAM: $8B (US K-12 digital learning market)
- SAM: $1.2B (math-specific tools for grades 6-8)
- SOM: $24M (2% of SAM by Year 3)

Sizing Method: Bottom-up (180K teachers × $400/teacher/year) + value theory (time savings)

❌ **Bad:**
"Our market is anyone who needs medication tracking. The healthcare market is huge - over $3 trillion."
- Problems: No specificity, TAM too broad, no user/buyer distinction, no realistic sizing

❌ **Bad:**
"Target market: Hospitals and patients."
- Problems: Too vague, no quantification, no segmentation, no sizing methodology

### Validation Rules:

1. **Character Limit**: Market description ≤ 300 characters
2. **Quantification**: All market sizes include $ value or customer count
3. **User/Buyer Clarity**: Explicitly state if same or different
4. **SAM Validation**: SAM should be 10-50% of TAM (if wider variance, justify)
5. **SOM Realism**: SOM should be 1-10% of SAM for early-stage ventures
6. **Methodology Documentation**: At least one sizing method clearly described
7. **Segment Specificity**: Can describe the "perfect first customer" in detail

---

## SECTION B5: Business Model and Revenue

### Exact Format:

```markdown
## Section B5: Business Model
**Character Limit:** 300 characters maximum

**Revenue Model:**
[Describe how the project generates revenue]

**Revenue Streams:**
1. [Stream 1]
2. [Stream 2]
3. [Stream 3]

**Unit Economics:**
- **Customer Acquisition Cost (CAC):** [Amount]
- **Lifetime Value (LTV):** [Amount]
- **LTV:CAC Ratio:** [Ratio]

**Quality Checklist:**
- [ ] Revenue model is under 300 characters
- [ ] Revenue streams are listed
- [ ] Unit economics are quantified
- [ ] Business model is sustainable

---
```

### Content Requirements:

**Revenue Model Description (300 characters max):**
- Must specify HOW you charge (subscription, one-time, usage-based, freemium)
- Must specify WHO pays (end user, enterprise, third party)
- Should include pricing tier structure if applicable
- Should note primary revenue stream vs. secondary
- Must be realistic for stage (don't claim 5 revenue streams at idea stage)

**Revenue Streams:**

List 1-3 revenue streams in priority order.

**Common Models:**
- **Subscription (SaaS)**: Monthly/annual recurring (e.g., $99/month per teacher)
- **Usage-based**: Pay per transaction/API call (e.g., $0.10 per prescription filled)
- **License fee**: One-time or annual enterprise license (e.g., $50K per hospital per year)
- **Freemium**: Free tier + paid premium features (e.g., free for 5 users, $20/user after)
- **Marketplace/Transaction**: Take rate on transactions (e.g., 15% of tutoring session fee)
- **Advertising**: Revenue from ads shown to users
- **Data licensing**: Aggregate anonymized data sold to third parties

**Unit Economics:**

**Customer Acquisition Cost (CAC):**
- Total sales + marketing spend / # customers acquired
- Should include fully-loaded costs (salaries, tools, ads)
- Specify BLENDED vs. PAID CAC if using multiple channels
- Early-stage estimate acceptable if no customers yet
- Format: "$X per customer" or "$X per user"

**Lifetime Value (LTV):**
- Revenue per customer over entire relationship
- Formula: (Average monthly revenue per customer) × (Average customer lifespan in months) × (Gross margin %)
- Should account for churn/retention
- Format: "$X per customer"

**LTV:CAC Ratio:**
- Healthy SaaS: 3:1 or higher
- Acceptable: 2:1 to 3:1
- Warning sign: < 2:1 (unsustainable)
- Investor preference: 4:1 or higher
- Format: "X:1" (e.g., "3.5:1")

**Examples:**

✅ **Good (295 characters):**
"Annual SaaS subscription model: $5,000 per hospital per year for up to 500 patients, $8 per additional patient. Hospitals pay annually (Year 1), auto-renew with 3% price increase. Secondary revenue from anonymized adherence data licensing to pharmaceutical companies (10% of revenue)."

Revenue Streams:
1. Annual hospital subscriptions ($5K base + $8/patient overage) - 90% of revenue
2. Anonymized data licensing to pharma companies - 10% of revenue

Unit Economics:
- CAC: $1,200 per hospital (6-month sales cycle, $80K sales team cost / 67 hospitals/year)
- LTV: $18,000 per hospital (avg 3.6 year retention × $5K/year)
- LTV:CAC Ratio: 15:1

✅ **Good (289 characters):**
"Freemium model: Free for individual teachers (up to 30 students). School district licenses at $400/teacher/year (minimum 25 teachers). Pricing tiers: $8K for 25 teachers, $15K for 50, $25K for 100. Districts pay annually with net-30 terms. Premium features: advanced analytics, API access."

Revenue Streams:
1. District annual licenses ($400/teacher, minimum 25 teachers) - 95% of revenue
2. Enterprise API access for assessment companies - 5% of revenue

Unit Economics:
- CAC: $200 per teacher (district deals, inside sales)
- LTV: $1,600 per teacher (4-year average retention × $400/year)
- LTV:CAC Ratio: 8:1

❌ **Bad:**
"We'll make money from subscriptions, advertising, data sales, enterprise licenses, and consulting services."
- Problems: Too many streams (unrealistic), no pricing, no specifics, no unit economics

❌ **Bad:**
"Revenue model: TBD based on market feedback."
- Problems: No business model defined, not actionable

### Validation Rules:

1. **Character Limit**: Revenue description ≤ 300 characters
2. **Pricing Specificity**: Includes at least one specific price point with unit ($/month, $/year)
3. **Stream Prioritization**: Streams listed in revenue % order (largest first)
4. **Stream Realism**: ≤ 3 streams for early-stage (Idea-Pilot), ≤ 5 streams for Growth stage
5. **CAC Credibility**: CAC amount justified with calculation or benchmark
6. **LTV Credibility**: LTV based on realistic retention/churn assumptions
7. **Ratio Health**: LTV:CAC ≥ 2:1 (if lower, must explain path to improvement)
8. **Payment Terms**: Clear on when/how customer pays (monthly/annual/upfront)

---

## SECTION B6: Traction and Validation

### Exact Format:

```markdown
## Section B6: Traction and Validation
**Character Limit:** 300 characters maximum

**Current Status:**
[Describe current state of the project]

**Key Metrics:**
- **Metric 1:** [Value]
- **Metric 2:** [Value]
- **Metric 3:** [Value]

**Validation Evidence:**
- **Customer Interviews:** [Number]
- **Pilot Users:** [Number]
- **Paying Customers:** [Number]
- **Revenue to Date:** [Amount]

**Quality Checklist:**
- [ ] Status description is under 300 characters
- [ ] Key metrics are quantified
- [ ] Validation evidence is documented
- [ ] All claims are supported by numbers

---
```

### Content Requirements:

**Current Status Description (300 characters max):**
- Must state current maturity stage clearly (Idea, Prototype, Pilot, Early Commercialization, Growth)
- Must describe what EXISTS NOW (not future plans)
- Should include most recent milestone achieved
- Should note any active pilots, users, or revenue
- Must be honest (over-claiming destroys credibility)

**Key Metrics:**

Select 3-5 metrics appropriate for your stage:

**Idea Stage:**
- Problem discovery interviews conducted
- Problem severity ratings from interviews
- Hours spent on customer research
- Target customer access established

**Prototype Stage:**
- Prototype iterations completed
- User tests conducted
- Feedback points collected
- Feature validation rate (% of features validated as valuable)

**Pilot Stage:**
- Active pilot users
- User retention rate
- Engagement frequency (sessions/week)
- Pilot completion rate

**Early Commercialization:**
- Paying customers
- Monthly Recurring Revenue (MRR) or Annual Recurring Revenue (ARR)
- Customer acquisition rate (new customers/month)
- Net Promoter Score (NPS)
- Churn rate

**Growth Stage:**
- Total customers
- Revenue growth rate (MoM or YoY)
- Customer lifetime value (LTV)
- Gross margin %
- Expansion revenue rate

**Validation Evidence:**

Must quantify ALL validation activities:

**Customer Interviews:**
- Number conducted
- Date range (e.g., "18 interviews, Oct-Dec 2024")
- Segments covered (e.g., "6 nurses, 8 administrators, 4 patients")

**Pilot Users:**
- Current active pilots
- Pilot duration (e.g., "25 users, 90-day pilot")
- Pilot structure (paid vs. free, commitment level)

**Paying Customers:**
- Current paying customer count
- Customer type (e.g., "3 hospitals, 1 home health agency")
- Contract value/duration if available

**Revenue to Date:**
- Total revenue earned (not projected)
- Revenue breakdown if multiple streams
- Time period (e.g., "$47K in 6 months, Jan-Jun 2025")

**Examples:**

✅ **Good (298 characters):**
"Prototype stage: Working MVP tested with 25 elderly patients across 3 facilities (Dec 2024-Jan 2025). Completed 40 user interviews (20 patients, 12 nurses, 8 caregivers). 80% of pilot users report improved adherence. No paying customers yet; preparing for first paid pilot (Feb 2025)."

Key Metrics:
- Pilot completion rate: 88% (22/25 patients completed 90-day pilot)
- Engagement: 4.2 medication logs per day per patient
- User satisfaction: 8.5/10 average rating

Validation Evidence:
- Customer Interviews: 40 (20 patients, 12 nurses, 8 family caregivers, Oct-Dec 2024)
- Pilot Users: 25 (3 facilities, 90-day pilot, Dec 2024-Jan 2025)
- Paying Customers: 0 (first paid pilot starts Feb 2025)
- Revenue to Date: $0

✅ **Good (285 characters):**
"Early Commercialization: 12 paying school districts (127 teachers, 3,800 students). Live since Sept 2024. $51K ARR. Average teacher uses platform 3.2x per week. 85% renewal rate (3 renewals completed). NPS 67. Adding 2-3 districts per month. Product roadmap based on customer feedback."

Key Metrics:
- Paying customers: 12 districts (127 teachers)
- ARR: $51,000
- Teacher engagement: 3.2 sessions/week average
- Student active users: 3,200 (84% of total)
- Net Promoter Score: 67

Validation Evidence:
- Customer Interviews: 85 (45 teachers, 25 administrators, 15 students, Jun-Dec 2024)
- Pilot Users: 45 teachers (free pilots, Apr-Aug 2024)
- Paying Customers: 12 districts (Sept 2024-present)
- Revenue to Date: $38,250 (Sept 2024-Jan 2025)

❌ **Bad:**
"We have great traction with lots of interest. Many people want to use our product. We've talked to customers and they love it."
- Problems: No numbers, vague claims, no evidence, not verifiable

❌ **Bad:**
"10,000 users signed up for our waitlist."
- Problems: Waitlist ≠ validation; no usage, no payment, no engagement metrics

### Validation Rules:

1. **Character Limit**: Status description ≤ 300 characters
2. **Quantification**: ALL claims include numbers (no "many", "several", "lots")
3. **Recency**: All evidence dated within past 6 months (if older, explain)
4. **Stage Appropriateness**: Metrics match claimed stage (don't claim Growth with 0 revenue)
5. **Evidence Hierarchy**: Prioritize: Paying customers > Active users > Pilot users > Interviews
6. **Honesty Requirement**: "0" or "None" is acceptable and builds trust
7. **Interview Depth**: If claiming interviews, must have ≥ 10 for credibility
8. **Pilot Quality**: Pilots should be ≥ 30 days to be meaningful

---

## SECTION B7: Team and Resources

### Exact Format:

```markdown
## Section B7: Team
**Character Limit:** 200 characters maximum

**Team Overview:**
[Describe the core team]

**Key Team Members:**
1. **[Name]** - [Role]: [Relevant experience]
2. **[Name]** - [Role]: [Relevant experience]
3. **[Name]** - [Role]: [Relevant experience]

**Team Strengths:**
- [Strength 1]
- [Strength 2]
- [Strength 3]

**Quality Checklist:**
- [ ] Team description is under 200 characters
- [ ] Key team members are listed with relevant experience
- [ ] Team strengths are identified
- [ ] Team composition is appropriate for project stage

---
```

### Content Requirements:

**Team Overview (200 characters max - NOTE: SHORTER THAN OTHER SECTIONS):**
- Must state team SIZE (number of co-founders, full-time, part-time)
- Must summarize RELEVANT domain expertise
- Should note time commitment level (full-time, nights/weekends)
- Should mention any advisors if strategically important
- Must be concise (50% shorter than other sections)

**Key Team Members:**

List 2-5 core team members:

**Format per member:**
- **Full Name** - Title/Role: 1-sentence relevant background

**What to Include:**
- Prior experience directly relevant to THIS venture
- Domain expertise (industry knowledge, technical skills)
- Demonstrated success (prior exits, publications, leadership)
- Complementary skill sets across team

**What to Exclude:**
- Generic credentials irrelevant to venture ("MBA from Harvard" unless relevant)
- Accomplishments unrelated to THIS problem/solution
- Team members with minor roles or peripheral involvement

**Team Strengths:**

List 3-5 strengths that make THIS TEAM uniquely qualified for THIS VENTURE:

**Examples of Strong Strengths:**
- "15 years combined hospital IT implementation experience"
- "Published researchers in medication adherence (3 peer-reviewed papers)"
- "Prior edtech startup exit ($12M acquisition, 2022)"
- "Advisory board includes 2 CMOs from target hospitals"
- "Native access to target customer segment (founders are ICU nurses)"

**Weak/Generic Strengths:**
- "Passionate about the problem"
- "Hardworking and dedicated"
- "Strong technical skills"
- "Great communicators"

**Examples:**

✅ **Good (198 characters):**
"3 co-founders, full-time since Jan 2025. Combined 18 years hospital IT + clinical experience. Prior startup experience (1 exit). 2 advisors: CMO (major hospital system), pharma adherence researcher."

Key Team Members:
1. **Sarah Chen** - CEO: 8 years hospital IT implementations, former VP Product at EHR startup (acquired 2023)
2. **Dr. James Rodriguez** - Chief Medical Officer: ICU physician, published researcher in geriatric medication management
3. **Alex Kim** - CTO: 6 years healthcare software engineering, led HIPAA-compliant systems at prior company

Team Strengths:
- Direct clinical experience with target patient population (Dr. Rodriguez: 12 years ICU)
- Proven hospital IT sales/implementation experience (Sarah: sold to 40+ hospitals)
- Healthcare compliance expertise (Alex: built 3 HIPAA-compliant systems)
- Advisor network provides customer access (CMO advises, oversees 5 hospitals)

✅ **Good (194 characters):**
"2 co-founders full-time, 1 part-time engineer. 15 years combined K-12 teaching (8 years middle school math). Previous edtech experience (instructor at Coursera). Math education PhDs (both founders)."

Key Team Members:
1. **Dr. Maria Santos** - CEO: Middle school math teacher (8 years), PhD in Math Education, designed curriculum adopted by 50+ schools
2. **Dr. Priya Patel** - Chief Learning Officer: High school math teacher (7 years), PhD in Educational Psychology, published research on adaptive learning

Team Strengths:
- First-hand knowledge of teacher pain points (15 years classroom experience)
- Academic expertise in learning science (2 PhDs, 5 published papers on math education)
- Existing relationships with school districts (curriculum adoption in 50+ schools)
- Understanding of district procurement process (navigated adoptions successfully)

❌ **Bad:**
"Our team is passionate and experienced with diverse backgrounds. We have what it takes to succeed."
- Problems: No specifics, no names, no relevant experience stated, generic claims

❌ **Bad:**
"John Smith - CEO: MBA from Stanford, 10 years consulting at McKinsey"
- Problems: Credentials don't relate to venture, no domain expertise, no reason THIS person for THIS problem

### Validation Rules:

1. **Character Limit**: Team overview ≤ 200 characters (SHORTER than other sections)
2. **Relevance Requirement**: Every team member's description must connect to THIS venture
3. **Commitment Clarity**: State full-time vs. part-time vs. advisor explicitly
4. **Strength Specificity**: Each strength must be unique to this team (not generic trait)
5. **Completeness**: For stage Prototype+, must have technical + domain + business skills represented
6. **Founder Count**: 2-4 co-founders ideal (1 = risk, 5+ = too many)
7. **Advisor Realism**: Only list advisors who actively contribute (not just names)

---

## Maturity Stage Classification

### Required Classification

Every Executive Brief must classify the project into ONE of five maturity stages:

```markdown
## Maturity Assessment

### Current Stage
- [ ] IDEA
- [ ] PROTOTYPE
- [ ] PILOT
- [ ] EARLY_COMMERCIALIZATION
- [ ] GROWTH

### Technology Readiness Level (TRL)
**Current TRL:** [1-9]

**TRL Scale:**
- TRL 1-3: Basic research and concept development
- TRL 4-6: Technology development and validation
- TRL 7-9: System demonstration and deployment

---
```

### Stage Definitions and Criteria

#### IDEA Stage

**Characteristics:**
- Concept exists but no working prototype
- Problem identified through observation or personal experience
- Limited customer discovery (< 10 interviews)
- No users testing the solution
- Team is part-time or forming

**Required Evidence:**
- Problem statement backed by research or experience
- At least 5 customer discovery interviews
- Initial solution concept sketched

**TRL Range:** 1-3 (Basic principles observed, concept formulated)

**Example:**
"We've identified that elderly patients forget medications based on family experience and 8 initial interviews with caregivers. We have wireframes for an app concept but no working code."

---

#### PROTOTYPE Stage

**Characteristics:**
- Working prototype exists (can be low-fidelity)
- Problem validated through 10+ interviews
- Solution tested with 5-15 users for feedback
- Team has technical capability demonstrated
- No paying customers yet

**Required Evidence:**
- Functional prototype (code, mockup, physical model)
- 10+ problem validation interviews
- 5+ solution validation tests with real users
- User feedback documented

**TRL Range:** 4-6 (Component/subsystem validation, prototype demonstration)

**Example:**
"We have a working mobile app tested with 12 elderly patients over 30 days. Collected feedback on usability. Validated core features work. No paying customers; preparing first pilot."

---

#### PILOT Stage

**Characteristics:**
- Pilot program(s) active with real users
- 15-50 active users testing in realistic conditions
- Structured feedback collection in place
- Iterating based on pilot learnings
- May have LOIs (Letters of Intent) but limited/no revenue

**Required Evidence:**
- Active pilot with ≥ 15 users for ≥ 30 days
- Engagement metrics tracked
- At least 1 iteration based on pilot feedback
- Documented pilot results

**TRL Range:** 6-7 (System prototype demonstration in relevant environment)

**Example:**
"Three hospital pilots running with 45 total patients. 90-day pilot period. Tracking adherence, usability, and caregiver satisfaction. Two hospitals issued LOIs for paid contracts starting Q2."

---

#### EARLY_COMMERCIALIZATION Stage

**Characteristics:**
- First paying customers secured (1-20 customers)
- Revenue generated (even if small)
- Sales process established and repeatable
- Product stabilized (core features complete)
- Team includes sales/marketing capability

**Required Evidence:**
- ≥ 1 paying customer with signed contract
- ≥ $1K revenue earned (not just committed)
- Documented sales process
- Customer retention ≥ 60%

**TRL Range:** 7-8 (System complete and qualified through test/demonstration)

**Example:**
"12 paying hospital customers, $51K ARR. Live since Sept 2024. 85% renewal rate. Adding 2-3 customers per month. Clear sales process with 6-month average sales cycle."

---

#### GROWTH Stage

**Characteristics:**
- Product-market fit achieved
- Revenue scaling (≥ 20 customers or ≥ $200K ARR)
- Team scaling (hiring in progress)
- Repeatable, efficient customer acquisition
- Focus on optimization and expansion

**Required Evidence:**
- ≥ 20 paying customers OR ≥ $200K ARR
- Growth rate ≥ 10% month-over-month for 3+ months
- LTV:CAC ratio ≥ 3:1
- Gross margin ≥ 60%

**TRL Range:** 8-9 (System proven in operational environment)

**Example:**
"127 paying customers, $940K ARR, growing 18% monthly. Team of 22. LTV:CAC of 4.2:1. Expanding to second market segment. Preparing Series A fundraise."

---

### Technology Readiness Level (TRL) Detailed Scale

**TRL 1 - Basic principles observed**
- Fundamental research
- Scientific observation of basic principles

**TRL 2 - Technology concept formulated**
- Practical applications identified
- Concept documented

**TRL 3 - Experimental proof of concept**
- Laboratory tests
- Analytical studies

**TRL 4 - Technology validated in lab**
- Component validation in lab environment
- Standalone prototype

**TRL 5 - Technology validated in relevant environment**
- Testing in simulated or actual environment
- Component integration

**TRL 6 - Technology demonstrated in relevant environment**
- Prototype system tested in relevant environment
- Engineering-scale model

**TRL 7 - System prototype demonstrated in operational environment**
- Full prototype in operational environment
- Near-final configuration

**TRL 8 - System complete and qualified**
- Actual system completed and qualified through testing
- Proven to work in operational environment

**TRL 9 - Actual system proven in operational environment**
- Full-scale production and deployment
- System proven through successful operations

---

## Evidence Tracking

### Evidence Log (Required)

```markdown
## Evidence Tracking

### Evidence Log
| Evidence ID | Section | Source Type | Quality Rating | Description | Date |
|-------------|---------|-------------|----------------|-------------|------|
| E001 | B2 | Interview Notes | 3 | Customer interviews with 18 nurses | 2024-10-15 |
| E002 | B6 | Usage Analytics | 4 | Pilot user engagement data (n=25) | 2025-01-10 |
| E003 | B4 | Industry Report | 5 | Gartner Healthcare IT Report 2024 | 2024-11-01 |

**Quality Rating Scale:**
- **5 - Gold Standard:** Published research, audited financials, signed contracts
- **4 - Strong:** Multiple customer testimonials, verified metrics
- **3 - Moderate:** Single-source testimonials, founder-reported metrics
- **2 - Weak:** Anecdotal evidence, unverified claims
- **1 - Very Weak:** No supporting evidence

---
```

### Evidence Requirements by Section

**B1 (Project Name):**
- Evidence Type: Trademark search, domain registration, brand assets
- Quality: 3+ (documented brand)

**B2 (Problem Statement):**
- Evidence Type: Customer interviews, market research, industry reports, published studies
- Quality: 4+ for Legitimacy validation
- Minimum: 10+ interviews or credible third-party research

**B3 (Solution):**
- Evidence Type: Prototype screenshots, demo video, code repository, feature documentation
- Quality: 3+ (working prototype or detailed spec)

**B4 (Market):**
- Evidence Type: Industry reports (Gartner, Forrester), government statistics, bottom-up calculations
- Quality: 4+ (third-party validation of market size)

**B5 (Business Model):**
- Evidence Type: Pricing interviews, competitive benchmarking, unit economics calculations
- Quality: 3+ (validated with customers or comparables)

**B6 (Traction):**
- Evidence Type: Analytics dashboards, signed agreements, financial records, user testimonials
- Quality: 4-5 (verified metrics, contractual commitments)

**B7 (Team):**
- Evidence Type: LinkedIn profiles, publications, prior company records, references
- Quality: 4+ (publicly verifiable credentials)

---

## Output Formats

### Markdown Format (.md) - Primary

**File Naming Convention:**
```
Executive_Brief_[ProjectName]_[YYYY-MM-DD].md
```

**Examples:**
- `Executive_Brief_MediTrack_2025-01-15.md`
- `Executive_Brief_EduLearn_2025-02-01.md`

**Markdown Requirements:**
- Use standard Markdown syntax (compatible with GitHub, Notion, Obsidian)
- Header levels: H1 for title, H2 for major sections, H3 for subsections
- Use **bold** for labels, *italic* for emphasis sparingly
- Use `code blocks` for data, formulas, or technical terms
- Tables must use proper alignment (| --- | --- |)
- Checkboxes formatted as `- [ ]` for unchecked, `- [x]` for checked
- Horizontal rules: three dashes `---`

---

### DOCX Format (.docx) - Optional

**When Required:**
- Formal submission to investors or evaluation committees
- Integration with existing organizational Word-based processes
- Situations requiring tracked changes or comments

**File Naming Convention:**
```
Executive_Brief_[ProjectName]_[YYYY-MM-DD].docx
```

**DOCX Formatting Standards:**

**Styles:**
- Title: Calibri 18pt, Bold
- Heading 1: Calibri 16pt, Bold
- Heading 2: Calibri 14pt, Bold
- Body text: Calibri 11pt
- Character limits: Arial Narrow 10pt (to show count)

**Page Setup:**
- Margins: 1 inch all sides
- Orientation: Portrait
- Page numbers: Bottom center, starting on page 2

**Color Scheme:**
- Headers: Dark blue (#1F4788)
- Section dividers: Light gray (#D3D3D3)
- Alerts/Red flags: Red (#C00000)
- Pass/Success: Green (#00B050)

**Tables:**
- Style: Grid Table 4 - Accent 1
- Header row: Bold, shaded
- Borders: All cells

**Character Count Display:**
For each limited section, show count:
"One-Line Description (142/150 characters)"

---

## Validation Checklist

Before finalizing any Executive Brief, verify ALL 45 items below:

### Document Structure (7 items)
- [ ] 1. Title is exactly "# Executive Brief Template"
- [ ] 2. Project Information section present with all 4 fields
- [ ] 3. Date in YYYY-MM-DD format
- [ ] 4. Executive Brief ID in format EB-YYYY-NNN
- [ ] 5. All seven B-sections (B1-B7) present
- [ ] 6. Maturity Assessment section present
- [ ] 7. Evidence Log present with ≥ 3 entries

### B1: Project Name and Tagline (4 items)
- [ ] 8. Project name is official, consistent name (not generic)
- [ ] 9. One-line tagline present
- [ ] 10. Combined name + tagline ≤ 150 characters
- [ ] 11. Tagline explains WHAT and FOR WHOM

### B2: Problem Statement (6 items)
- [ ] 12. Problem description ≤ 300 characters
- [ ] 13. Problem is solution-neutral (no "app", "platform", "AI", etc.)
- [ ] 14. At least 2 quantified metrics (%, $, time, count)
- [ ] 15. Severity rating (1-5) provided and justified
- [ ] 16. Frequency specified with timeframe
- [ ] 17. Affected population includes SIZE (number + unit)

### B3: Solution Overview (5 items)
- [ ] 18. Solution description ≤ 300 characters
- [ ] 19. Clear connection to problem statement
- [ ] 20. Solution type selected (Product/Service/Platform/Other)
- [ ] 21. 3-5 key features listed
- [ ] 22. Features are user-facing (not technical architecture)

### B4: Market and Users (6 items)
- [ ] 23. Market description ≤ 300 characters
- [ ] 24. User/buyer distinction explicitly stated
- [ ] 25. TAM, SAM, SOM all quantified with $ or user count
- [ ] 26. At least one sizing methodology documented
- [ ] 27. SAM is 10-50% of TAM (or variance justified)
- [ ] 28. SOM is 1-10% of SAM for early-stage

### B5: Business Model (5 items)
- [ ] 29. Revenue model description ≤ 300 characters
- [ ] 30. At least one specific price point stated ($/month, $/year, etc.)
- [ ] 31. 1-3 revenue streams listed in priority order
- [ ] 32. CAC, LTV, and LTV:CAC ratio all provided
- [ ] 33. LTV:CAC ratio ≥ 2:1 (or path to improvement stated)

### B6: Traction and Validation (6 items)
- [ ] 34. Status description ≤ 300 characters
- [ ] 35. 3-5 key metrics quantified
- [ ] 36. Customer interview count provided (or "0" if none)
- [ ] 37. Pilot user count provided (or "0" if none)
- [ ] 38. Paying customer count provided (or "0" if none)
- [ ] 39. All claims include numbers (no "many", "several", "some")

### B7: Team and Resources (3 items)
- [ ] 40. Team overview ≤ 200 characters (NOTE: shorter limit)
- [ ] 41. 2-5 key team members listed with relevant experience
- [ ] 42. 3-5 team strengths that are specific to THIS venture

### Maturity Assessment (3 items)
- [ ] 43. One maturity stage selected (Idea/Prototype/Pilot/Early Commercialization/Growth)
- [ ] 44. TRL level (1-9) specified
- [ ] 45. Stage selection matches evidence in B6 (Traction)

---

## Common Mistakes to Avoid

### Top 15 Mistakes (Learn from these!)

**1. Exceeding Character Limits**
- ❌ Problem: Writing 450 characters when limit is 300
- ✅ Solution: Write first, then ruthlessly edit. Every word must earn its place.
- **Tip:** Use character counter tool; aim for 90-95% of limit (not 100%)

**2. Solution Language in Problem Statement**
- ❌ Problem: "Patients lack a mobile app for medication tracking"
- ✅ Solution: "Patients forget 40% of prescribed medication doses, leading to 125K hospitalizations annually"
- **Why it matters:** Solution bias prevents objective problem validation

**3. Vague, Unquantified Claims**
- ❌ Problem: "Many users love our product"
- ✅ Solution: "25 pilot users, 88% completion rate, NPS of 72"
- **Why it matters:** Investors can't evaluate "many" or "love"

**4. Unrealistic Market Sizing**
- ❌ Problem: "TAM is the entire $3 trillion healthcare industry"
- ✅ Solution: "TAM $12B (medication adherence), SAM $3B (US hospitals 200+ beds), SOM $90M (3% by Year 3)"
- **Why it matters:** Credibility destroyed by absurd TAM claims

**5. Too Many Revenue Streams Too Early**
- ❌ Problem: Idea-stage company claiming 6 different revenue streams
- ✅ Solution: 1-2 revenue streams for Idea/Prototype, 2-3 for Pilot/Early Commercial
- **Why it matters:** Lack of focus signals inexperience

**6. Marketing Jargon Over Substance**
- ❌ Problem: "Revolutionary AI-powered synergistic ecosystem"
- ✅ Solution: "Mobile app that sends medication reminders and tracks completion"
- **Why it matters:** Jargon obscures what you actually do

**7. Confusing Users and Buyers**
- ❌ Problem: Not distinguishing between end user and economic buyer
- ✅ Solution: "Users: Nurses and patients. Buyers: Hospital IT directors."
- **Why it matters:** Sales/marketing strategy depends on this distinction

**8. Claiming Traction That Isn't Traction**
- ❌ Problem: "5,000 people on our waitlist"
- ✅ Solution: "25 active pilot users, 12 paying customers"
- **Why it matters:** Waitlist ≠ validation; usage and payment = validation

**9. Irrelevant Team Credentials**
- ❌ Problem: "CEO has MBA from Harvard"
- ✅ Solution: "CEO: 8 years hospital IT sales, sold to 40+ hospitals"
- **Why it matters:** Domain expertise > general credentials

**10. No Evidence Documentation**
- ❌ Problem: Claims with zero supporting evidence
- ✅ Solution: Every claim linked to evidence (interviews, data, contracts)
- **Why it matters:** Unsubstantiated claims = assumption, not validation

**11. Inconsistent Project Names**
- ❌ Problem: "MediTrack" in header, "MediTrak App" in B1, "The Company" in B3
- ✅ Solution: One official name used consistently throughout
- **Why it matters:** Inconsistency suggests lack of attention to detail

**12. Stage Misclassification**
- ❌ Problem: Claiming "Growth stage" with 0 revenue
- ✅ Solution: Honest stage classification matching actual traction
- **Why it matters:** Over-claiming destroys credibility instantly

**13. Generic, Non-Specific Features**
- ❌ Problem: "User-friendly interface, cloud-based, scalable"
- ✅ Solution: "Photo-based dose verification, real-time caregiver alerts, pharmacy integration"
- **Why it matters:** Features must differentiate, not describe table stakes

**14. Unsustainable Unit Economics**
- ❌ Problem: LTV:CAC of 0.8:1 with no plan to improve
- ✅ Solution: LTV:CAC of 3:1, or <3:1 with clear path to improvement
- **Why it matters:** Bad unit economics = non-viable business

**15. Missing Quality Checklists**
- ❌ Problem: Sections marked complete without checkbox validation
- ✅ Solution: All checkboxes reviewed and checked (or issue noted)
- **Why it matters:** Checklists catch errors before submission

---

## Red Flag Checklist

Evaluators should flag Executive Briefs with ANY of these issues:

### Critical Red Flags (Stop/Major Revision Required)
- [ ] **Character limits exceeded by >20%** (shows inability to follow constraints)
- [ ] **Problem statement includes solution language** (fundamental flaw)
- [ ] **No quantified claims** (all assertions vague/qualitative)
- [ ] **Market sizing missing or absurd** (TAM > $1T or no SAM/SOM)
- [ ] **Zero evidence for any claim** (no interviews, data, metrics)
- [ ] **Team has no relevant domain expertise** (generic backgrounds)
- [ ] **Stage miscategorized by >1 level** (claiming Growth with idea-stage traction)
- [ ] **Business model undefined or incoherent** (no clear revenue source)

### Warning Flags (Address Before Proceeding)
- [ ] **< 10 customer interviews** (insufficient problem validation)
- [ ] **User = buyer not addressed** (B2B ventures)
- [ ] **LTV:CAC < 2:1** (unsustainable economics)
- [ ] **No paying customers at Early Commercial stage** (stage mismatch)
- [ ] **>3 revenue streams at Idea/Prototype stage** (lack of focus)
- [ ] **Evidence quality ratings all ≤ 2** (weak validation)
- [ ] **Team all part-time at Pilot+ stage** (commitment question)

### Quality Flags (Strengthen Before Next Stage)
- [ ] **Top-down market sizing only** (no bottom-up validation)
- [ ] **Single source evidence** (need corroboration)
- [ ] **No competitive analysis** (market understanding gap)
- [ ] **Pilot < 30 days or < 15 users** (insufficient pilot scope)
- [ ] **Features list is all technical** (not user-centric)

---

## Quality Assurance Process

### Pre-Submission Review (Self-Assessment)

**Step 1: Completeness Check (5 minutes)**
- [ ] All 7 B-sections present
- [ ] All required subsections filled (no "[TBD]" placeholders)
- [ ] Evidence log has ≥ 3 entries
- [ ] Maturity assessment completed

**Step 2: Character Limit Verification (5 minutes)**
- [ ] B1: ≤ 150 characters (name + tagline combined)
- [ ] B2: ≤ 300 characters (problem description)
- [ ] B3: ≤ 300 characters (solution description)
- [ ] B4: ≤ 300 characters (market description)
- [ ] B5: ≤ 300 characters (revenue model)
- [ ] B6: ≤ 300 characters (status description)
- [ ] B7: ≤ 200 characters (team overview)

**Step 3: Quantification Audit (10 minutes)**
Go through each section and highlight every claim. Verify each claim has:
- [ ] A number (%, $, count, time period)
- [ ] A source (evidence reference)
- [ ] Appropriate precision (not false precision)

**Step 4: Coherence Check (10 minutes)**
- [ ] B3 solution addresses B2 problem
- [ ] B4 market size supports B5 revenue projections
- [ ] B6 traction matches claimed maturity stage
- [ ] B7 team has skills needed for B3 solution

**Step 5: Red Flag Scan (5 minutes)**
Review all Red Flag Checklist items above.
- [ ] Zero critical red flags
- [ ] ≤ 2 warning flags (with mitigation plan)

**Total QA Time: ~35 minutes**

---

### Peer Review Checklist (If Available)

When having a colleague review your Executive Brief:

**Ask reviewer to assess:**
1. **Clarity**: "Can you understand what this company does in 60 seconds?"
2. **Credibility**: "Which claims seem unsubstantiated?"
3. **Coherence**: "Do the sections tell a consistent story?"
4. **Character limits**: "Are any sections too long or obviously cut off?"
5. **Quantification**: "Which claims lack numbers?"

**Provide reviewer:**
- This format specification document
- 15 minutes of their time
- Permission to be brutally honest

---

## File Naming and Version Control

### File Naming Convention

**Format:**
```
Executive_Brief_[ProjectName]_[YYYY-MM-DD].[extension]
```

**Rules:**
- **ProjectName**: No spaces (use CamelCase or underscores)
- **Date**: ISO format YYYY-MM-DD (sorts chronologically)
- **Extension**: .md (primary) or .docx (optional)

**Examples:**
- `Executive_Brief_MediTrack_2025-01-15.md`
- `Executive_Brief_EduLearn_2025-02-01.md`
- `Executive_Brief_AgriSense_2025-03-10.docx`

**Version Control:**
- Use date in filename (auto-versions)
- Don't use "v1", "v2", "final", "final_final"
- Git commit messages should reference Brief ID (EB-2025-001)

---

### Storage and Organization

**Recommended folder structure:**
```
/vianeo-evaluations/
  /step0-executive-briefs/
    Executive_Brief_MediTrack_2025-01-15.md
    Executive_Brief_MediTrack_2025-02-10.md  (updated version)
    Executive_Brief_EduLearn_2025-01-20.md
  /step3-market-maturity/
  /step9-value-network/
  /evidence/
    /EB-2025-001/  (MediTrack evidence)
      interview_notes_oct2024.pdf
      pilot_results_jan2025.xlsx
    /EB-2025-002/  (EduLearn evidence)
```

---

## Integration with VIANEO Framework

### How Step 0 Feeds Other Steps

**Step 0 → Step 1 (Problem Legitimacy):**
- B2 (Problem Statement) provides problem definition
- B6 (Validation Evidence) provides interview count for Q8, Q13

**Step 0 → Step 2 (40Q Assessment):**
- B sections provide baseline information for all 40 questions
- Evidence log provides starting point for evidence gathering

**Step 0 → Step 3 (Market Maturity):**
- B4 (Market) provides market sizing for questions
- B6 (Traction) provides customer interview/validation data
- Maturity stage determines expected validation depth

**Step 0 → Steps 4-8:**
- Provides consistent project summary across all evaluations
- Ensures all evaluators working from same factual foundation

---

### When to Update Executive Brief

**Required Updates:**
- New maturity stage reached (e.g., Prototype → Pilot)
- Major traction milestone (first paying customer, significant user growth)
- Pivot in problem, solution, or market
- Significant team changes (co-founder join/departure)
- Every 6 months minimum (keeps information current)

**Version Control Best Practice:**
- Create new file with new date
- Update Brief ID version if major revision (EB-2025-001v2)
- Maintain prior versions for historical record
- Update evidence log with new evidence

---

## Appendix: Character Counting Reference

### Character Limit Summary Table

| Section | Character Limit | What Counts |
|---------|----------------|-------------|
| B1: Project Name + Tagline | 150 | Combined total |
| B2: Problem Description | 300 | Description text only |
| B3: Solution Description | 300 | Description text only |
| B4: Market Description | 300 | Description text only |
| B5: Revenue Model | 300 | Description text only |
| B6: Current Status | 300 | Description text only |
| B7: Team Overview | 200 | Description text only |

**What counts as a character:**
- Letters: a-z, A-Z
- Numbers: 0-9
- Punctuation: . , ! ? ; : ' "
- Spaces between words
- Line breaks (if within the description field)

**What does NOT count:**
- Section headers (## Section B2)
- Labels (**Problem Description:**)
- Checkbox lists
- Table structures
- Horizontal rules (---)

**Tools for counting:**
- Word processors: Select text, check character count (include spaces)
- Online: CharacterCountOnline.com, LetterCount.com
- Code editors: Many show character count in status bar

---

## Appendix: Example Executive Briefs

### Example 1: MediTrack (Prototype Stage)

```markdown
# Executive Brief Template

## Project Information
**Project Name:** MediTrack
**Date Prepared:** 2025-01-15
**Prepared By:** Assessment Team
**Executive Brief ID:** EB-2025-001

---

## Section B1: Project Name and Tagline
**Character Limit:** 150 characters maximum

**Project Name:**
MediTrack

**One-Line Tagline:**
AI-powered medication adherence monitoring for elderly patients with chronic conditions

[Character count: 9 + 84 = 93/150]

---

## Section B2: Problem Statement
**Character Limit:** 300 characters maximum

**Problem Description:**
Elderly patients with 5+ chronic conditions forget medication doses 40% of the time, leading to 125K hospitalizations annually in the US. Current paper logs are lost or filled incorrectly. Family caregivers lack visibility, discovering problems only during crises.

[Character count: 295/300]

**Problem Characteristics:**
- **Severity:** 5 (life-threatening complications, preventable hospitalizations)
- **Frequency:** Daily (40% of doses missed, avg 3.2 missed doses per patient per week)
- **Affected Population:** 8M elderly Americans with 5+ chronic conditions, 12M family caregivers

---

## Section B3: Solution Overview
**Character Limit:** 300 characters maximum

**Solution Description:**
Mobile app that sends personalized medication reminders, tracks dose completion via photo confirmation, and alerts family caregivers when doses are missed. Simple tap-based interface for limited tech literacy. Syncs with pharmacies for automated prescription updates.

[Character count: 298/300]

**Solution Type:**
- [x] Product (Mobile Application)

**Key Features:**
1. Personalized medication reminders synced to prescription schedules
2. Photo-based dose verification and completion tracking
3. Real-time caregiver alerts for missed medications
4. Pharmacy integration for automated prescription updates
5. Simple tap-based interface designed for elderly users

---

## Section B4: Market and Users
**Character Limit:** 300 characters maximum

**Target Market:**
US hospitals with 200+ beds (2,500 facilities) serving elderly patients with chronic conditions. Secondary: home health agencies, assisted living. Users (nurses, patients) differ from buyers (hospital administrators). Initial focus: 100 hospitals in Northeast region.

[Character count: 299/300]

**User/Buyer Distinction:**
- **Primary Users:** Nurses (dose administration tracking), elderly patients (compliance)
- **Primary Buyers:** Hospital IT directors, Chief Medical Officers
- **Are users and buyers the same?** [ ] Yes [x] No

**Market Sizing:**
- **TAM:** $12B (global medication adherence market)
- **SAM:** $3B (US hospitals 200+ beds)
- **SOM:** $90M (3% of SAM by Year 3)

**Sizing Method:**
- [x] Bottom-up (2,500 hospitals × 300 patients avg × $400/patient/year)

---

## Section B5: Business Model
**Character Limit:** 300 characters maximum

**Revenue Model:**
Annual SaaS subscription: $5,000 per hospital per year for up to 500 patients, $8 per additional patient. Hospitals pay annually (Year 1), auto-renew with 3% annual increase. Secondary revenue from anonymized adherence data licensing to pharmaceutical companies (10% of revenue).

[Character count: 295/300]

**Revenue Streams:**
1. Annual hospital subscriptions ($5K base + $8/patient overage) - 90% of revenue
2. Anonymized data licensing to pharma companies - 10% of revenue

**Unit Economics:**
- **CAC:** $1,200 per hospital (6-month sales cycle)
- **LTV:** $18,000 per hospital (3.6 year avg retention × $5K/year)
- **LTV:CAC Ratio:** 15:1

---

## Section B6: Traction and Validation
**Character Limit:** 300 characters maximum

**Current Status:**
Prototype stage: Working MVP tested with 25 elderly patients across 3 facilities (Dec 2024-Jan 2025). Completed 40 user interviews (20 patients, 12 nurses, 8 caregivers). 80% of pilot users report improved adherence. No paying customers yet; preparing for first paid pilot (Feb 2025).

[Character count: 298/300]

**Key Metrics:**
- **Pilot completion rate:** 88% (22/25 patients completed 90-day pilot)
- **Engagement:** 4.2 medication logs per day per patient
- **User satisfaction:** 8.5/10 average rating

**Validation Evidence:**
- **Customer Interviews:** 40 (20 patients, 12 nurses, 8 family caregivers, Oct-Dec 2024)
- **Pilot Users:** 25 (3 facilities, 90-day pilot, Dec 2024-Jan 2025)
- **Paying Customers:** 0 (first paid pilot starts Feb 2025)
- **Revenue to Date:** $0

---

## Section B7: Team
**Character Limit:** 200 characters maximum

**Team Overview:**
3 co-founders, full-time since Jan 2025. Combined 18 years hospital IT + clinical experience. Prior startup experience (1 exit). 2 advisors: CMO (major hospital system), pharma adherence researcher.

[Character count: 198/200]

**Key Team Members:**
1. **Sarah Chen** - CEO: 8 years hospital IT implementations, former VP Product at EHR startup (acquired 2023)
2. **Dr. James Rodriguez** - Chief Medical Officer: ICU physician, 12 years experience, published researcher in geriatric medication management
3. **Alex Kim** - CTO: 6 years healthcare software engineering, led HIPAA-compliant systems at prior company

**Team Strengths:**
- Direct clinical experience with target patient population (Dr. Rodriguez: 12 years ICU)
- Proven hospital IT sales/implementation (Sarah: sold to 40+ hospitals)
- Healthcare compliance expertise (Alex: built 3 HIPAA-compliant systems)
- Advisor network provides customer access (CMO oversees 5 target hospitals)

---

## Evidence Tracking

### Evidence Log
| Evidence ID | Section | Source Type | Quality Rating | Description | Date |
|-------------|---------|-------------|----------------|-------------|------|
| E001 | B2 | Interview Notes | 3 | Patient/caregiver interviews (n=28) | 2024-10-15 |
| E002 | B6 | Usage Analytics | 4 | Pilot user engagement data (n=25) | 2025-01-10 |
| E003 | B4 | Industry Report | 5 | Gartner Healthcare IT Report 2024 | 2024-11-01 |
| E004 | B7 | Public Records | 5 | LinkedIn profiles, prior company acquisition | 2025-01-05 |
| E005 | B5 | Pricing Study | 3 | Hospital willingness-to-pay interviews (n=8) | 2024-12-20 |

---

## Maturity Assessment

### Current Stage
- [ ] IDEA
- [x] PROTOTYPE
- [ ] PILOT
- [ ] EARLY_COMMERCIALIZATION
- [ ] GROWTH

**Justification:** Working MVP tested with 25 users, 40+ interviews conducted, no paying customers yet. Preparing for first paid pilot.

### Technology Readiness Level (TRL)
**Current TRL:** 6

**TRL Scale:**
- TRL 1-3: Basic research and concept development
- TRL 4-6: Technology development and validation ← CURRENT
- TRL 7-9: System demonstration and deployment

**TRL 6 Justification:** Prototype demonstrated in relevant environment (3 hospital facilities) with real users (25 elderly patients). Engineering-scale model validated but not yet in full operational deployment.

---
```

---

## Summary

This format specification ensures that every Step 0 Executive Brief output:

1. **Follows exact structural requirements** for professional consistency
2. **Adheres to character limits** to enforce clarity and conciseness
3. **Maintains solution-neutral problem statements** to prevent solution bias
4. **Quantifies all claims** with evidence-backed assertions
5. **Aligns maturity stage** with actual traction and validation
6. **Enables consistent evaluation** across the VIANEO framework

**Total specification length:** ~3,200 words

**Key takeaway:** The Executive Brief is not marketing—it's evidence-based extraction of core project facts in a standardized format that enables rapid, fair, and consistent evaluation.

---

**End of Format Specification**
