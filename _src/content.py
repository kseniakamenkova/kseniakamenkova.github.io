"""All site copy, taken from the Figma file "Portfolio" (hUhHsZ8Pk8y2OU47MkWVLf).

Text keeps Figma's line breaks: "\n" is a line break, "\n\n" an empty line.
Rows refer to image rows in rows.json (by page and index).
"""

LINKEDIN = "https://www.linkedin.com/in/ksenia-kamenkova-319421298"
CV = "https://voracious-sponge-c0d.notion.site/Kseniia-Kamenkova-3ff7068607728109b769cb983cbfbc4b"
TELEGRAM = "https://t.me/kskamenkova"
SKYENG = "https://skyeng.ru/"

HOME = {
    "title": "Ksenia Kamenkova — Senior Product Designer",
    "description": "Senior Product Designer with 5 years of experience designing digital products for web and mobile: onboarding, conversion, referrals and payments.",
    "name": "Hi, I’m Ksenia",
    "intro": [
        "Senior Product Designer with 5 years of experience designing digital products for web and mobile. I work across different parts of the product journey, from acquisition and onboarding to conversion, referrals and payments.",
        "I enjoy solving complex problems, turning chaos into structure, and finding solutions that work for both users and the business.",
    ],
    # Order follows the Figma grid (left to right, top to bottom).
    "cards": [
        {
            "slug": "onboarding", "year": "2026", "label": "mobile app onboarding", "img": "card-onb",
            "crop": {"box": (58, 6, 193, 388), "img": ("323.55%", "120.7%", "-112.37%", "-10.31%")},
            "mcrop": {"box": (-1, -21, 205, 412), "img": ("323.55%", "120.7%", "-112.37%", "-10.31%")},
            "text": "Onboarding redesign for kids and adults. Goal: increase conversion from the first screen to application. I owned every stage of the work, from building the CJM to designing a new visual language and coordinating with other teams.",
            "metrics": [("+1.4 pp", "application conversion"), ("+21%", "cash-in")],
        },
        {
            "slug": "payment-widget", "year": "2024", "label": "payment widget", "img": "card-pay",
            "crop": {"box": (0, 0, 272, 400), "img": ("231.37%", "118%", "-58.09%", "-9%")},
            "mcrop": {"box": (-67, -26, 287, 325), "img": ("231.37%", "153.22%", "-58.09%", "-11.69%")},
            "text": "Redesign of the payment widget and rollout of installment payments across all of the school’s products. Goal: build a new, flexible widget and increase payment conversion. I was responsible for the development and design at all stages.",
            "metrics": [("+15%", "people completing payment"), ("+6%", "conversion from lead to payment")],
        },
        {
            "slug": "product-catalog", "year": "2026", "label": "product catalog", "img": "card-cat",
            "crop": {"box": (-1, 0, 295, 400), "img": ("211.53%", "117%", "-51.86%", "-8.5%")},
            "mcrop": {"box": (-73, -33, 323, 438), "img": ("211.53%", "117%", "-51.86%", "-8.5%")},
            "text": "Redesign of the product catalog in the student’s personal account, aimed at increasing repeat purchases and retention. I worked across every stage, from helping a new product manager get up to speed on the legacy catalog and building the CJM to designing every user flow.",
            "metrics": [("+3%", "increased recurrent revenue to monthly base")],
        },
        {
            "slug": "referral", "year": "2025", "label": "referral program", "img": "card-ref",
            "crop": {"box": (-3, 0, 272, 400), "img": ("229.41%", "117%", "-56.25%", "-9%")},
            "mcrop": {"box": (-67, -26, 277, 408), "img": ("229.41%", "117%", "-56.25%", "-9%")},
            "mmetrics": [("4% → 11%", "new revenue through referrals"), ("-18%", "CAC")],
            "text": "Design of a new referral program. Goal: increase engagement with the program and grow revenue from the referral channel. I owned the research and design at every stage and across every touchpoint, for both referrers and invited users.",
            "metrics": [("4% → 11%", "new revenue through referrals"), ("-18%", "customer acquisition cost")],
        },
    ],
}

# Block types used on case pages:
#   ("section", heading, [body...])       heading on the left, body on the right with a vertical line
#   ("row", n)                            image row n (1-based) from rows.json, full-bleed band if it has one
#   ("image", src, w, h, radius, alt)     single image in the content column
# Body items:
#   ("p", text) ("callout", label, text) ("points", [text...]) ("metrics", [(value, label)...])
#   ("groups", [(subheading, text) or (subheading, text, [list items], text_after)...])
#   ("also", [items...]) ("review", name, role, photo, text)

CASES = {
    "onboarding": {
        "title": "Mobile app onboardings for adults and kids",
        "meta": ["redesign", "skyeng", "2026"],
        "description": "Onboarding redesign for the Skyeng mobile app: +1.4 pp application conversion and +21% cash-in.",
        # Phone layout (Figma frame "onboarding page" mobile, 949:11089): order of pieces, in groups.
        # intro:N = Overview / My role / Key metrics, block:N = item N of "blocks", mrow:N = phone-only carousel N.
        "mobile": [
            ["intro:0", "intro:1", "mrow:1", "intro:2"],
            ["block:1", "mrow:2", "block:3", "mrow:3", "block:5"],
            ["block:8"],
        ],
        "intro": [
            ("section", "Overview", [
                ("p", "Skyeng is the largest EdTech platform in Russia, helping both adults and children achieve their learning goals."),
                ("callout", "CHALLENGE", "Thousands of students use the Skyeng app, but many of them drop off before finishing onboarding or stay on the free plan afterwards. Our goal was to increase onboarding completion and conversion to application, and to grow the number of students who find the right product for them and go on to make a purchase."),
            ]),
            ("section", "My role", [
                ("points", [
                    "Led end-to-end design, competitor research, analyzed existing experience and designed new flows and user scenarios",
                    "Developed a new visual language together with marketing team",
                    "Owned the product copy and content structure, working with UX-writers to ensure clarity and accuracy",
                    "Worked with a Project manager, Head of Product Design, mobile engineering and marketing",
                ]),
            ]),
            ("section", "Key metrics after launch", [
                ("metrics", [("+1.4 pp", "application conversion"), ("+14%", "first screen → application"), ("+21%", "Cash-In during the A/B test period")]),
            ]),
        ],
        "blocks": [
            ("row", 1),
            ("section", "Process", [
                ("groups", [("SEARCH", "To set our direction, I conducted competitor research and analyzed the existing user experience. This helped us to understand which features and patterns were already familiar to users, which UX/UI solutions worked well or bad, and what we could adopt from our existing onboarding flows.")]),
            ]),
            ("image", "/assets/img/onboarding/flow.webp", 1152, 660, 16, "Onboarding user flows"),
            ("section", "Process", [
                ("groups", [
                    ("ANALYZED AND PREPARED SOLUTIONS", "After several brainstorming sessions with the Product Manager and Design Lead, I developed two alternative user flows: one with a shorter onboarding process and a quick quiz, and another with more screens featuring stories about the school. \nWe debated which approach would work better. The shorter flow allowed users to move through onboarding faster, while the longer one helped build trust in the school and increase the likelihood of purchasing a course.\nAfter weighing the pros and cons of both approaches, we decided to find a compromise by combining the best elements of each flow into one."),
                    ("ADDED USER SEGMENTATION", "To better understand users’ needs and recommend products that matched their educational goals, I added a quiz to segment users. The quiz was adapted from the web funnel, where it had already demonstrated strong results, and tailored to fit the app onboarding experience."),
                    ("NEW DESIGN", "To increase user engagement, I decided to completely redesign the onboarding experience by introducing mascots and creating new illustrations in collaboration with the Marketing team. These visual elements became part of the overall product identity and are now used across other communication channels."),
                ]),
            ]),
            ("row", 2),
            ("section", "Process", [
                ("groups", [("PERSONALIZED OFFERS AND UPSELL", "After completing the quiz, users received personalized offers based on their answers. This helped them find what they were looking for and allowed us to increase revenue through upselling.\n\nI also designed a personalized card for each product, highlighting its key features and the benefits of applying now. This encouraged users to submit applications sooner, increasing conversions while reducing the operational costs of acquiring customers through this channel.")]),
            ]),
            ("row", 3),
            ("section", "Results", [
                ("p", "As a result, we achieved better results than expected, and we rolled out the onboarding to 100% of our users."),
                ("metrics", [("+1.4 pp", "application conversion"), ("+14%", "First screen → application"), ("+21%", "Cash-In during the A/B test period")]),
            ]),
            ("section", "Review", [
                ("review", "Valentin Filatov", "Product manager · ex-Skyeng", "/assets/img/reviews/onb.webp",
                 "I was a Product Manager at Skyeng, and Ksenia and I worked together on redesigning the onboarding experience for the mobile app. Ksenia conducted competitor research, brought all the onboarding screens, including quizzes, together into a cohesive picture, and proposed several onboarding flows and branching options. She also clearly explained the differences between them, which made it much easier for us to make decisions.\n\nThe project had a tight deadline and a high level of uncertainty, but Ksenia worked quickly and effectively while maintaining a high quality of work.\n\nAs a result, an A/B test of the new onboarding increased application conversion by 1.4 percentage points, significantly exceeding the target of 0.3 percentage points, and we rolled it out to all users.\n\nI would highly recommend Ksenia as a designer who takes full ownership of complex challenges and drives them through to results."),
            ]),
        ],
    },
    "referral": {
        "title": "Referral program for both users:\nreferrers and\u00a0referred",
        "meta": ["redesign", "skyeng", "2025"],
        "wide_title": True,
        "description": "A unified, points-based referral program for Skyeng: referral revenue grew from 4% to 11%, blended CAC down 18%.",
        # Phone layout (Figma frame "referral page" mobile, 971:17430). The Results metrics sit in the intro, as "Metrics after launch".
        "mobile": [
            ["intro:0", "intro:1", "mrow:1", "block:7"],
            ["block:1", "mrow:2", "block:3", "mrow:3", "block:5", "mrow:4"],
            ["block:8"],
        ],
        "mobile_titles": {"block:7": "Metrics after launch"},
        "intro": [
            ("section", "Overview", [
                ("p", "Skyeng's original referral program rewarded both the referrer and the referred user with free lessons.\nAs the school expanded its offering to include structured courses, the existing referral model became less suitable. Skyeng introduced a separate, cash-based referral program specifically for course students."),
                ("callout", "CHALLENGE", "Both programs were no longer delivering the desired results, while maintaining them required significant resources from multiple teams. \nOur challenge was to unify both programs into a single solution that would work for all students, simplify reward management, increase user engagement, and drive more revenue through referrals."),
            ]),
            ("section", "My role", [
                ("points", [
                    "Led end-to-end design, competitor research, analyzed existing experience and designed new flows and user scenarios for both sides: referrers and referred users",
                    "Designed the end-to-end referral experience across key product flows and touchpoints including supporting communications Email and Stories",
                    "Owned the product copy and content structure, working with UX-writers to ensure clarity and accuracy",
                    "Collaborated closely with the Head of Skyeng, Head of Product Growth, Product Manager, Marketing and Engineering teams.",
                ]),
            ]),
            ("section", "Key metrics after launch", [
                ("metrics", [("4% → 11%", "New revenue through referrals"), ("-18%", "Blended Customer Acquisition Cost"), ("0.6% → 1%", "Referral program MAU")]),
            ]),
        ],
        "blocks": [
            ("row", 1),
            ("section", "Process", [
                ("groups", [
                    ("ANALYZED EXISTING REFERRAL PROGRAMS", "To define our referral strategy, I analyzed existing referral programs. I mapped every user path, for both referrers and referred users which helped us understand the current issues with the referral program and identify opportunities for growth. Based on that, I suggested ideas to improve our referral program."),
                    ("SEARCH", "Conducted competitor research to understand which features and patterns were already familiar to users, which UX/UI solutions worked well or poorly, and what we could adopt."),
                ]),
            ]),
            ("row", 2),
            ("section", "Process", [
                ("groups", [
                    ("KEY FINDINGS AND OPPORTUNITIES", "After analyzing insights from UX research, competitor analysis, and user research conducted by our research team, we identified several key pain points and opportunities for improvement:", [
                        "User engagement with the referral program declined, reducing their motivation to recommend the school to others.",
                        "Students were less inclined to recommend the school solely for personal gain. Their primary motivation was often the desire to help others.",
                        "Students lacked sufficient information about how the referral program worked and what benefits both the referrer and the referred user would receive.",
                        "We identified opportunities to strengthen existing entry points and introduce new when students would be more likely to share a referral link, such as after completing a homework assignment.",
                    ], None),
                    ("CREATED NEW REWARD SYSTEM", "Instead of having two separate referral programs, we consolidated them into a single points-based system that worked for all students.\nThis created a flexible, centrally managed rewards system that could work with different promotions, discounts, and products across the school. Students earned points directly in their accounts and could redeem them for other products offered by the school."),
                    ("REDESIGNED THE REFERRAL EXPERIENCE", "Redesigned the referral experience, introducing new UI patterns and elements. Users could track the status of their invitations, see how many points they had earned, and access the showcase to spend their points."),
                ]),
            ]),
            ("row", 3),
            ("section", "Process", [
                ("groups", [
                    ("DESIGNED NEW LANDINGS PAGES", "Created dedicated landing pages for both adult and kids’ products, giving invited users relevant information, an explanation of how the referral program works, and a clear path to apply."),
                    ("CREATED A NEW TOOL FOR MARKETING", "These landing pages and the referral page in the personal account became key tools for the marketing team to communicate promotional campaigns and special offers to users."),
                    ("DESIGNED EMAILS AND STORIES", "I designed a series of emails and in-app stories to communicate the new referral program, encourage participation, and increase user engagement."),
                ]),
            ]),
            ("row", 4),
            ("section", "Results", [
                ("metrics", [
                    ("4% → 11%", "New revenue through referrals"),
                    ("-18%", "Blended Customer Acquisition Cost"),
                    ("0.6% → 1%", "Referral program MAU"),
                    ("1.12", "Average invitations per active referrer"),
                    ("60% MAU", "Visited the referral program at least once"),
                    ("20% MAU", "Copied the invitation link at least once"),
                ]),
            ]),
            ("section", "Review", [
                ("review", "Aleksandr Balin", "Head of Product Growth · ex\u2011Skyeng", "/assets/img/reviews/ref.webp",
                 "I highly recommend Ksenia to any tech company where user experience is a serious business priority. She combines excellent product taste with a strong commercial instinct.\n\nWe worked together at Skyeng on several projects, most notably the redesign of our referral programme. It was a high-priority initiative with a direct impact on business performance.\nKsenia redesigned the end-to-end customer journey for both referrers and referred users, helping drive 60% programme adoption and contributing 11% of all new revenue through referrals.\n\nA strong product designer who understands how good experience translates into business results."),
            ]),
        ],
    },
    "product-catalog": {
        "title": "Product catalog in the student's personal account",
        "meta": ["skyeng", "2026"],
        "description": "A self-service product catalog in the Skyeng student account that grew monthly recurring revenue by 3%.",
        # Phone layout, following the onboarding and referral mobile frames (no Figma phone frame for this page yet).
        # Carousels reuse the desktop screens at the phone carousel height (524px).
        "mobile": [
            ["intro:0", "intro:1", "mrow:1", "intro:2"],
            ["block:1", "mrow:2", "block:3", "mrow:3", "block:5", "mrow:4"],
            ["block:7"],
        ],
        # Desktop shows the metrics once, as "Results" near the top; phones keep the heading used on the other pages.
        "mobile_titles": {"intro:2": "Key metrics after launch"},
        "wide_title": True,
        "intro": [
            ("section", "Overview", [
                ("callout", "CHALLENGE", "The product catalog was designed to solve several problems:\n\n• Increase the share of repeat purchases by making additional products and learning opportunities more visible\n• Bring Skyeng and Skysmart products together in one place, so students could explore available programs and learning formats and choose the ones that suit them\n• Let students quickly buy a product for another student\n• Lay the groundwork for a full shopping cart and the further development of self-service purchases"),
            ]),
            ("section", "My role", [
                ("points", [
                    "Led design, competitor research, analyzed the existing experience, ran user research, and designed the end-to-end customer journey from product discovery to purchase",
                    "Developed a new visual language for the catalog",
                    "Collaborated closely with Design Lead, Product Manager and Engineering throughout the project",
                ]),
            ]),
            ("section", "Results", [
                ("metrics", [("+3%", "Increased monthly recurring revenue by 3% by launching a self-service product catalog, with no increase in cost of sales and no drop in ATV")]),
                ("also", [
                    "The catalog was reused in the B2B funnel on the Ozon marketplace, increasing course purchases",
                    "The catalog became the basis for the catalog on the Skysmart homepage, letting prospective students explore and buy products",
                ]),
            ]),
        ],
        "blocks": [
            ("row", 1),
            ("section", "Process", [
                ("groups", [
                    ("SEARCH", "Conducted competitor research to understand which features and patterns were already familiar to users, which UX/UI solutions worked well or poorly, and what we could adopt."),
                    ("UNMODERATED USABILITY TESTING", "Together with the research team, we explored how users discover products and what influences their purchasing decisions across different user journeys. The research revealed that pricing was one of the key decision-making factors, while users rarely explored filters beyond the basic options.\nThese insights helped us refine the catalog experience and prioritize the features to include in the first iteration."),
                ]),
            ]),
            ("row", 2),
            ("section", "Process", [
                ("groups", [
                    ("DESIGNED NEW CATALOG EXPERIENCE", "I completely redesigned the existing experience, adding detailed product cards, filters, search, and favorites. We also automated product card creation, eliminating the need for manual input by the editorial team."),
                    ("DEVELOPED A NEW VISUAL LANGUAGE", "I created the visual language and a recognizable style for each product, making product information easier to scan and understand. Designed the hero images for each product, establishing a visual foundation that the Marketing team later built upon to expand and evolve product cards across other channels."),
                ]),
            ]),
            ("row", 3),
            ("section", "Process", [
                ("groups", [
                    ("PURCHASE FOR OTHER STUDENTS", "The catalog was expanded to include products for a wide range of learning goals and connected with the option to purchase products for other students, helping expand our student base while reducing reliance on the Sales team."),
                    ("ADDED A NEW TOOL FOR MARKETING", "The Marketing team can now use the catalog to promote campaigns and special offers."),
                    ("EXPANDED BEYOND THE PERSONAL ACCOUNT", "The catalog became the base for a catalog on the main Skysmart page, allowing prospective students to explore products and make purchase, and reusing the catalog in B2B funnel at Ozon marketplace which increased course purchases."),
                ]),
            ]),
            ("row", 4),
            ("section", "Review", [
                ("review", "Ekaterina Gavrilova", "Product Manager · Skyeng", "/assets/img/reviews/cat.webp",
                 "I worked with Ksenia on launching self-pay service product calatog and on subscription renewals project, with many edge cases.\n\nShe works through every user story and asks the right questions, making sure she understands the problem before she proposes a design solution. She also doesn’t freeze and wait for the ready answers when some data or context is missing. She has excellent design taste, always thinks about both users and the business, and is very comfortable to work with.\n\nWhichever team gets her next will be extremely lucky."),
            ]),
        ],
    },
    "payment-widget": {
        "title": "Payment widget",
        "meta": ["redesign", "skyeng", "2024"],
        "description": "A flexible payment widget with installment payments for Skyeng and Skysmart: +15% of users complete payment.",
        "wide_title": True,
        "intro": [
            ("section", "Overview", [
                ("callout", "CHALLENGE", "The existing payment widget lacked the flexibility. We couldn't prioritize preferred payment methods, promote installment payments, or tailor the payment options to different business needs. Additionally, the widget lacked dedicated space for information about each payment method, making it harder for users to understand and compare their options.\n\nWe needed to build a new, more flexible payment widget that could support new payment methods, provide greater control over their presentation, and improve the payment experience."),
            ]),
            ("section", "My role", [
                ("points", [
                    "Сonducted competitor research, analyzed the existing experience and designed the end-to-end customer journey from product selection to payment",
                    "Defined the structure of the payment widget and the logic for displaying different payment methods",
                    "Collaborated closely with the Product Owner, Product Managers, Engineering, Billing and Research teams throughout the project",
                ]),
            ]),
            ("section", "Key metrics after launch", [
                ("metrics", [
                    ("52.7% → 55.6%", "the widget-to-payment conversion has increased on desktop and (51.3% <b>→</b> 55.5% mobile)"),
                    ("+15%", "more users go from clicking ‘Buy’ to completing payment on desktop (+13% mobile)"),
                    ("+6%", "lead-to-payment conversion"),
                ]),
            ]),
        ],
        "blocks": [
            ("row", 1),
            ("section", "Process", [
                ("groups", [
                    ("SEARCH AND CONCEPT", "I started by conducting competitor research to identify familiar features and UX patterns, evaluate existing solutions, and explore opportunities to improve the payment experience.\nI then presented four design concepts to the team. Together, we selected two to validate through unmoderated user research."),
                    ("UNMODERATED CONCEPT TESTING", "Together with the research team, we explored how users perceived the design concepts, which layouts were easiest to understand, and what information mattered most to them.\nOne key finding was that users could scan popular payment methods more easily in a horizontal layout than in a vertical list. These findings informed the final layout and helped us prioritize the most relevant payment methods."),
                ]),
            ]),
            ("row", 2),
            ("section", "Process", [
                ("groups", [
                    ("DESIGNED NEW PAYMENT WIDGET", "Based on the research findings, I designed a new payment widget. I refreshed the UI, highlighted the three preferred payment methods, and moved the remaining options into a dropdown menu. I also added details about each payment method, including payment schedules where available, to help users choose the option that best suited their needs."),
                    ("ADDED SUPPORT FOR PROMO AND DISCOUNTS", "The widget now can supports various installment plans and promo offers, making relevant payment options more visible to users. It also automatically applies users’ existing reward points to their payments."),
                    ("BUILT A FLEXIBLE PAYMENT SYSTEM", "The billing team can add new payment methods and update payment information without design support. The widget automatically adapts to different payment methods, while the business can reorder preferred options based on its needs."),
                ]),
            ]),
            ("row", 3),
            ("section", "A/B test", [
                ("p", "We launched an A/B test and found that the new widget underperformed the existing one on mobile version. After analyzing the data and testing several hypotheses, we suspected that the issue was related to the navigation in the payment system part. \nI simplified the mobile navigation, and we ran the experiment again. This time, the new widget outperformed. Following the successful test, we rolled out the widget to all traffic across Skyeng and Skysmart."),
            ]),
            ("section", "Results", [
                ("metrics", [
                    ("52.7% → 55.6%", "the widget-to-payment conversion has increased on desktop and (51.3% <b>→</b> 55.5% mobile)"),
                    ("+15%", "more users go from clicking ‘Buy’ to completing payment on desktop (+13% mobile)"),
                    ("+6%", "lead-to-payment conversion"),
                ]),
            ]),
            ("section", "Review", [
                ("review", "Timofey Novikov", "Head of Skyeng", "/assets/img/reviews/pay.webp",
                 "I worked with Ksenia on multiple projects at Skyeng, and working with her was a pleasure.\n\nWhat I appreciate most about her is her meticulous attention to detail, ensuring every aspect of the product is user-friendly. She scrutinizes each step, every piece of copy, and every potential issue to guarantee a smooth user experience. While this level of detail can sometimes seem excessive, it is precisely what makes a product intuitive and accessible.\n\nKsenia's work extends beyond functionality; her interfaces are both elegant and consistent, reflecting careful planning and execution.\n\nShe also has a deep understanding of business objectives. Ksenia aligns her design choices with key performance metrics and is adept at discussing trade-offs with both product and engineering teams. A notable example is the payment widget, which initially underperformed in a mobile A/B test. Ksenia identified the issues, made necessary improvements, and the revised version subsequently succeeded.\n\nI would confidently recommend Ksenia as a product designer who excels in tackling complex challenges."),
            ]),
        ],
    },
}
