import requests
import json

# Define the URL of the API endpoint for creating kdramas
api_url = 'http://localhost:8000/kdrama/kdrama/'  

# Define data for each kdrama individually
kdramas = [
    {
        "title": "Descendants of the Sun",
        "description": "A love story between Captain Yoo Shi Jin, Korean Special Forces, and Doctor Kang Mo Yeon, surgeon at Haesung Hospital. Together they face danger in a war-torn country.",
        "release_year": "2016",
        "duration": "16 episodes"
    },
    {
        "title": "My Demon",
        "description": "\"My Demon\" revolves around the story of Do Do Hee, a chaebol heiress who seems to be everyone's enemy, and Jung Koo Won, a demon who loses his powers and ends up living with Do Do Hee.",
        "release_year": "2023",
        "duration": "16 episodes"
    },
    {
        "title": "Crash Landing on You",
        "description": "A paragliding mishap drops a South Korean heiress in North Korea -- and into the life of an army officer, who decides he will help her hide",
        "release_year": "2019",
        "duration": "16 episodes"
    },
    {
        "title": "Itaewon Class",
        "description": "In a colorful Seoul neighborhood, an ex-con and his friends fight a mighty foe to make their ambitious dreams for their street bar a reality.",
        "release_year": "2020",
        "duration": "16 episodes"
    },
    {
        "title": "Vincenzo",
        "description": "During a visit to his motherland, a Korean-Italian mafia lawyer gives an unrivaled conglomerate a taste of its own medicine with a side of justice.",
        "release_year": "2021",
        "duration": "20 episodes"
    },
    {
        "title": "Hospital Playlist",
        "description": "Every day is extraordinary for five doctors and their patients inside a hospital, where birth, death and everything in between coexist.",
        "release_year": "2020",
        "duration": "12 episodes"
    },
    {
        "title": "My Love from the Star",
        "description": "Do Minjun, an alien stranded on Earth for 400 years, discovers that a comet could be his chance to return home, but as he prepares for his journey, he falls in love with his neighbor Cheon Songyi, a famous actress.",
        "release_year": "2013",
        "duration": "21 episodes"
    },
    {
        "title": "Backstreet Rookie",
        "description": "A former troublemaker applies for a job at a convenience store owned by the same man who ran errands for her a few years ago.",
        "release_year": "2020",
        "duration": "16 episodes"
    },
    {
        "title": "Signal",
        "description": "A time-defying walkie-talkie connects 21st-century criminal profiler Park Hae-yeong with spunky detective Lee Jae-han in 1989. Together, they unravel mysteries from the past and present to reshape the future.",
        "release_year": "2016",
        "duration": "16 episodes"
    },
    {
        "title": "King the Land",
        "description": "King the Land tells the story of Gu Won (Lee Jun-ho) who is the heir of The King Group, a luxury hotel conglomerate, who was thrown into an inheritance war, and Cheon Sa-rang (Im Yoon-ah), a hotelier who always has a smile on her face till she meets Gu Won.",
        "release_year": "2023",
        "duration": "16 episodes"
    },
    {
        "title": "The King: Eternal Monarch",
        "description": "A modern-day Korean emperor passes through a mysterious portal and into a parallel world, where he encounters a feisty police detective.",
        "release_year": "2020",
        "duration": "16 episodes"
    },
    {
        "title": "Cheese in the Trap",
        "description": "Hong Seul, a third-year college student, just wants to get good grades and earn enough money for tuition. But when classmate Yoo Jung returns from the army, she is the only one sees past his pleasant veneer to the person who constantly causes trouble for her. Joo Yeon's harassment of Seol turns dangerous.",
        "release_year": "2016",
        "duration": "16 episodes"
    },
    {
        "title": "While You Were Sleeping",
        "description": "While You Were Sleeping is a combination of the romance, legal drama and fantasy genres, focusing on the tale of three young adults who have acquired the ability to see the future through their dreams.",
        "release_year": "2017",
        "duration": "32 episodes"
    },
    {
        "title": "Business Proposal",
        "description": "In disguise as her friend, Ha-ri shows up on a blind date to scare away her friend's prospective suitor, but plans go awry when he turns out to be Ha-ri's CEO -- and he makes a proposal.",
        "release_year": "2022",
        "duration": "12 episodes"
    },
    {
        "title": "Strong Girl Bong-soon",
        "description": "Do Bong-soon (Park Bo-young) was born with superhuman strength. Her strength is hereditary and passed along only to the women in her family. Her dream is to create a video game with herself as the main character.",
        "release_year": "2017",
        "duration": "16 episodes"
    },
    {
        "title": "Moon Lovers: Scarlet Heart Ryeo",
        "description": "When a total eclipse of the sun took place, a 21st century woman, is transported back in time to the Goryeo Dynasty of Korea, in the body of 16-year-old girl. There she witnesses love, rivalry, politics, and friendships ensue between the handsome princes, in a fight for the throne, friendship, and love.",
        "release_year": "2016",
        "duration": "20 episodes"
    },
    {
        "title": "Boys Over Flowers",
        "description": "This follows the story of Geum Jan-di, a high schooler from a struggling family who is admitted into a prestigious private academy after saving the life of a student there.",
        "release_year": "2009",
        "duration": "25 episodes"
    },
    {
        "title": "My ID is Gangnam Beauty",
        "description": "Kang Mi-rae (Im Soo-hyang) decides to get plastic surgery after years of being bullied because of her looks. Her \"rebirth\" seems successful at first, but as her life at the university unfolds, her plan starts to backfire.",
        "release_year": "2018",
        "duration": "16 episodes"
    },
    {
        "title": "W: Two Worlds",
        "description": "W centers on the clash between \"two worlds\": the real world and an alternate universe inside a webtoon, from which the title of the television series was taken.",
        "release_year": "2016",
        "duration": "16 episodes"
    },
    {
        "title": "Secret Garden",
        "description": "A rich young CEO falls for a poor stuntwoman despite class differences, cultural traditions and the man's firmly objecting mother.",
        "release_year": "2010",
        "duration": "20 episodes"
    }
]

# Iterate over each kdrama data and send a POST request for each one
for kdrama_data in kdramas:
    response = requests.post(url=api_url, data=json.dumps(kdrama_data), headers={'Content-Type': 'application/json'})

    if response.status_code == 201:
        print(f"Kdrama '{kdrama_data['title']}' created successfully.")
    else:
        print(f"Error creating kdrama '{kdrama_data['title']}': {response.content}")