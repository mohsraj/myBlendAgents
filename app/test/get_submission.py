def by_id(submission_id: str):
    """Retrieve a submission by its ID"""
    # This function would typically interact with a database or API to fetch the submission data
    # For this example, we will return a mock submission
    submiision_data = {
        "role": "user",
        "content": """
            {
            "QuestionaireId": "E8A750EB-AE61-4446-84FC-4AEF5B7C7DCA",
            "Section": [
                {
                    "SectionPrompt": "🎭 Your scent is an extension of your style. Let’s uncover the olfactory equivalent of your aesthetic.",
                    "Question": [
                        {
                            "QuestionType": "Multiple Choice",
                            "Question": "Would you describe your style as classic, casual, edgy, luxurious, or something else?",
                            "QuestionOption": [
                                {"QuestionOptionValue": "Trendy and fashionable"},
                                {"QuestionOptionValue": "Bold and expressive"},
                                {"QuestionOptionValue": "Simple and functional"},
                                {"QuestionOptionValue": "Casual and laid-back"},
                                {"QuestionOptionValue": "Polished and professional"},
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "610A709F-0C9D-494A-B849-1F2DCB6E045E",
                                    "questionAnswer": "15474aa2-5cb2-4eb9-bc0b-9e64c9936ed8",
                                },
                                {
                                    "SubmissionDataId": "0BD0BEA3-ED73-46A9-9544-F744ADCC21BA",
                                    "questionAnswer": "5d014f38-4099-4110-86a8-8340680b972f",
                                },
                            ],
                        },
                        {
                            "QuestionType": "Single Choice",
                            "Question": "What genre of music do you connect with most? How does it make you feel?",
                            "QuestionOption": [
                                {
                                    "QuestionOptionValue": "A mix of everything—depends on my mood"
                                },
                                {
                                    "QuestionOptionValue": "Current chart-toppers and trending playlists"
                                },
                                {
                                    "QuestionOptionValue": "Relaxing instrumental or timeless jazz"
                                },
                                {
                                    "QuestionOptionValue": "Pop and rock from the 90s or early 2000s"
                                },
                                {
                                    "QuestionOptionValue": "Classic hits from the 70s or 80s"
                                },
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "DB828CA6-BD45-4986-ADDB-41A9E8C5726B",
                                    "questionAnswer": "1d3b1977-535a-4cc5-ad39-52b910deab40",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Single Choice",
                            "Question": "What cuisine do you enjoy most—spicy, fresh, sweet, rich? Why?",
                            "QuestionOption": [
                                {"QuestionOptionValue": "Rich\/decadent"},
                                {"QuestionOptionValue": "Spicy"},
                                {"QuestionOptionValue": "Fresh\/healthy"},
                                {"QuestionOptionValue": "Sweet"},
                                {"QuestionOptionValue": "Savory"},
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "FE896D46-FCA8-481E-B34D-7B0AF935F48B",
                                    "questionAnswer": "ca61fb0a-4b9e-4734-bc84-2e0af95feea4",
                                }
                            ],
                        },
                    ],
                },
                {
                    "SectionPrompt": "🌍 Where do you feel most at home? Your surroundings hold clues to the scents you gravitate toward.",
                    "Question": [
                        {
                            "QuestionType": "Single Choice",
                            "Question": "Where outdoors do you feel most at home? Forest, beach, cityscape, mountains?",
                            "QuestionOption": [
                                {
                                    "QuestionOptionValue": "In a blooming garden filled with sunlight"
                                },
                                {
                                    "QuestionOptionValue": "In the quiet depths of a forest"
                                },
                                {
                                    "QuestionOptionValue": "By a calm lake reflecting the sky"
                                },
                                {
                                    "QuestionOptionValue": "On a mountain with crisp, cool air"
                                },
                                {"QuestionOptionValue": "On a wide, open meadow"},
                                {
                                    "QuestionOptionValue": "By the ocean with crashing waves"
                                },
                                {"QuestionOptionValue": "Under a starlit desert sky"},
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "3D6AE5C2-0FC5-4ED1-A38F-1C3C24BBE2D0",
                                    "questionAnswer": "17905fd8-22b0-4903-8e34-956cd6d1a900",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Color Picker",
                            "Question": "What color comes to mind when thinking of your favorite place? Why?",
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "D1C3E0EC-769D-4B27-A8B5-6C242A689B56",
                                    "questionAnswer": "#2fffdd",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Color Picker",
                            "Question": "What color would you choose for a special occasion? What does it say about you?",
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "8DB0D04C-2F54-4A26-A7F1-A371461956CD",
                                    "questionAnswer": "#14c286",
                                }
                            ],
                        },
                    ],
                },
                {
                    "SectionPrompt": "✨ Fragrance is an emotion in a bottle. What kind of presence do you want to carry with you?",
                    "Question": [
                        {
                            "QuestionType": "Single Choice",
                            "Question": "What first impression do you hope to leave? Confident, mysterious, approachable, elegant?",
                            "QuestionOption": [
                                {"QuestionOptionValue": "Mystery and allure"},
                                {"QuestionOptionValue": "Confidence and strength"},
                                {"QuestionOptionValue": "Warmth and comfort"},
                                {"QuestionOptionValue": "Curiosity and intrigue"},
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "B701236B-2133-4682-A620-B58C6A4A0413",
                                    "questionAnswer": "6b983a45-0d6a-4675-84e8-898669f2eb17",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Single Choice",
                            "Question": "Do you prioritize uniqueness, familiarity, luxury, or something else in personal choices?",
                            "QuestionOption": [
                                {"QuestionOptionValue": "Strength and practicality"},
                                {"QuestionOptionValue": "A balance of both"},
                                {"QuestionOptionValue": "Softness and elegance"},
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "8C6443DE-ECBA-404B-8BE7-0A169D79A1FB",
                                    "questionAnswer": "3de118a5-02af-4a77-9c17-ac10e792b7b3",
                                }
                            ],
                        },
                    ],
                },
                {
                    "SectionPrompt": "💡 Discover the essence of YOU. Your personality is like a fragrance—layered, expressive, and unique.",
                    "Question": [
                        {
                            "QuestionType": "Slider",
                            "Question": "Do you trust logic or instinct more when making decisions? Give an example.",
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "F6F15851-D9D4-46A5-9F02-ABE9DCE99A9E",
                                    "questionAnswer": "77",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Single Choice",
                            "Question": "Which element—earth, water, air, or fire—best represents you, and why?",
                            "QuestionOption": [
                                {
                                    "QuestionOptionValue": "Water: Fluid, adaptable, and ever-refreshing."
                                },
                                {
                                    "QuestionOptionValue": "Fire: Bold, passionate, and full of energy."
                                },
                                {
                                    "QuestionOptionValue": "Air: Light, free-spirited, and always in motion."
                                },
                                {
                                    "QuestionOptionValue": "Earth: Grounded, strong, and connected to the natural world."
                                },
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "FF5F1A5E-F92D-4C73-9DD3-06B7F50B84B6",
                                    "questionAnswer": "996b88f2-d21c-4500-a484-dbc8a7abdfda",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Single Choice",
                            "Question": "Imagine your personality as a texture—velvety, crisp, airy, smooth, rough, or something else? Describe it.",
                            "QuestionOption": [
                                {"QuestionOptionValue": "Gentle and comforting"},
                                {"QuestionOptionValue": "Light and free"},
                                {"QuestionOptionValue": "Firm and resilient"},
                                {"QuestionOptionValue": "Silky and seamless"},
                                {"QuestionOptionValue": "Raw and authentic"},
                                {"QuestionOptionValue": "Cool and composed"},
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "B50987DD-7480-4D73-9704-649545D73876",
                                    "questionAnswer": "3c4ef91c-6312-47c1-90c2-c37f1398f843",
                                }
                            ],
                        },
                    ],
                },
                {
                    "SectionPrompt": "🔮 A scent that fits seamlessly into your life. Let’s fine-tune the details to craft a scent that feels like second skin.",
                    "Question": [
                        {
                            "QuestionType": "Slider",
                            "Question": "Do you prefer a scent that is soft and intimate, bold and commanding, or something in between?",
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "4171CC5B-D828-46AB-A90D-F0E972CED985",
                                    "questionAnswer": "64",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Single Choice",
                            "Question": "Are you a planner or do you go with the flow? How does this affect your choices?",
                            "QuestionOption": [
                                {
                                    "QuestionOptionValue": "I prefer to keep things open and adapt as I go."
                                },
                                {
                                    "QuestionOptionValue": "I like to have everything planned and organized ahead of time."
                                },
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "E8C429B8-10F8-4589-AE5F-31A11D3E73FC",
                                    "questionAnswer": "9389553a-0477-4e9a-af73-26bf0b784a21",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Slider",
                            "Question": "How do you unwind—spa day, nature walk, socializing, reading?",
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "9DE9465D-B878-46EE-85B2-690B995A363B",
                                    "questionAnswer": "22",
                                }
                            ],
                        },
                    ],
                },
                {
                    "SectionPrompt": "This is an extra information about the person to be considered into the formula, (like weather, location, ...)",
                    "Question": [
                        {
                            "QuestionType": "Weather",
                            "Question": "The weather at the persons location",
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "E79C6F96-9DB5-4332-9D00-4C849A46B1D6",
                                    "questionAnswer": "From July to September, Istanbul, Turkiye experiences a warm summer season with the average temperature ranging between 20°C and 28°C. The humidity levels during this period are generally moderate, providing a comfortable atmosphere. The weather is predominantly sunny with a few instances of light rainfall, making it the driest season of the year. The overall atmosphere during this time is vibrant and lively, with long, sunny days and mildly cool evenings, perfect for outdoor activities and exploring the city's rich history and culture.",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Location",
                            "Question": "Do you feel more at home in vibrant cities full of energy and structure, or in peaceful natural spaces surrounded by greenery, earth, and tranquility? How does your everyday environment influence what feels comforting, inspiring, or authentic to you in a scent?",
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "B0F8E448-485E-4B90-806F-18A176C9E6BD",
                                    "questionAnswer": "Istanbul, Turkiye",
                                }
                            ],
                        },
                    ],
                },
                {
                    "SectionPrompt": "🌿 Your lifestyle shapes your scent. The way you move through life influences your perfect fragrance.",
                    "Question": [
                        {
                            "QuestionType": "Single Choice",
                            "Question": "What time of day do you feel most connected to yourself?",
                            "QuestionOption": [
                                {
                                    "QuestionOptionValue": "Late at night, when creativity and spontaneity take over."
                                },
                                {
                                    "QuestionOptionValue": "At sunrise, with fresh air and endless possibilities."
                                },
                                {
                                    "QuestionOptionValue": "As the evening unfolds, calm and reflective."
                                },
                                {
                                    "QuestionOptionValue": "In the afternoon, focused and immersed in the rhythm of the day."
                                },
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "680C4415-E3A9-45EF-AAEB-CB846E2E031A",
                                    "questionAnswer": "30b6c01b-c14b-4d63-a807-bd9c6a28aefd",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Slider",
                            "Question": "On a scale of 1 to 10, how energetic do you usually feel throughout the day?",
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "12F807B8-DE34-4A0C-B34B-B201F8534B0E",
                                    "questionAnswer": "80",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Single Choice",
                            "Question": "What's your ideal morning drink? Coffee, tea, juice, or something else? Describe the feeling it gives you.",
                            "QuestionOption": [
                                {"QuestionOptionValue": "A rich, bold espresso"},
                                {
                                    "QuestionOptionValue": "Freshly squeezed orange juice"
                                },
                                {"QuestionOptionValue": "A creamy vanilla latte"},
                                {"QuestionOptionValue": "A calming herbal tea"},
                                {"QuestionOptionValue": "A fruity smoothie"},
                                {"QuestionOptionValue": "A refreshing glass of water"},
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "C4798FAC-0685-43D2-B84A-DF4EA173A4E6",
                                    "questionAnswer": "585154cb-c921-4b1a-bf05-50a339a2a984",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Multiple Choice",
                            "Question": "How do you usually stay active? Gym, yoga, running, or something else?",
                            "QuestionOption": [
                                {"QuestionOptionValue": "Not very active"},
                                {"QuestionOptionValue": "Team sports"},
                                {"QuestionOptionValue": "Gym workouts"},
                                {"QuestionOptionValue": "Light walking"},
                                {"QuestionOptionValue": "Yoga"},
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "9DAD807C-9E76-4A6C-BF0F-5D89DF785382",
                                    "questionAnswer": "a4e1c882-816c-482d-bfc6-a3713f17691a",
                                },
                                {
                                    "SubmissionDataId": "1399DAEB-B8B9-4C3B-B60D-E3DA397D7BB0",
                                    "questionAnswer": "e32988a9-70ea-4ad5-871f-a9014ff2e71b",
                                },
                            ],
                        },
                        {
                            "QuestionType": "Multiple Choice",
                            "Question": "You have a free weekend. Would you rather stay in, explore, socialize, or do something else?",
                            "QuestionOption": [
                                {
                                    "QuestionOptionValue": "Hosting or attending a small gathering with close friends"
                                },
                                {
                                    "QuestionOptionValue": "Going on a road trip to explore new places"
                                },
                                {
                                    "QuestionOptionValue": "Dining at a fancy restaurant and indulging in gourmet dishes"
                                },
                                {
                                    "QuestionOptionValue": "Spending time at a spa or wellness retreat"
                                },
                                {
                                    "QuestionOptionValue": "Attending a live concert or theater show"
                                },
                                {
                                    "QuestionOptionValue": "Watching a movie or bingeing a new series at home"
                                },
                                {
                                    "QuestionOptionValue": "Shopping and strolling through a lively market"
                                },
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "83B36B08-5FD9-49F8-9844-FD9C3B3E678A",
                                    "questionAnswer": "5a1d4b85-933e-4c45-836e-0fb1764eac85",
                                }
                            ],
                        },
                        {
                            "QuestionType": "Single Choice",
                            "Question": "Describe a typical busy weekday. What keeps you moving?",
                            "QuestionOption": [
                                {
                                    "QuestionOptionValue": "My work involves hands-on tasks or being on-site."
                                },
                                {
                                    "QuestionOptionValue": "I'm often in meetings or managing a team."
                                },
                                {
                                    "QuestionOptionValue": "I focus on learning, studying, or developing new skills."
                                },
                                {
                                    "QuestionOptionValue": "I'm constantly on the move, visiting different locations."
                                },
                                {
                                    "QuestionOptionValue": "My day is flexible, and I set my own schedule."
                                },
                                {
                                    "QuestionOptionValue": "I spend most of my time working on a computer or behind a desk."
                                },
                                {
                                    "QuestionOptionValue": "I'm out and about, interacting with people face-to-face."
                                },
                            ],
                            "SubmissionData": [
                                {
                                    "SubmissionDataId": "E1724C98-0751-4A41-8DDB-FD760417FACB",
                                    "questionAnswer": "710c7ca7-0230-49fe-8cc8-979a3fbc21b5",
                                }
                            ],
                        },
                    ],
                },
            ],
        }""",
    }
    return submiision_data
