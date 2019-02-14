from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catagories, Games, Base, User

engine = create_engine('sqlite:///videogamescatalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create fake user
User1 = User(name="John Doe", email="jdplaceholder@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')  # noqa
session.add(User1)
session.commit()

# Action catagory and its initial items
catagory1 = Catagories(user_id=1, name='Action')

session.add(catagory1)
session.commit()

game1 = Games(user_id=1,
              name='Cuphead',
              catagory='Action',
              description='Cuphead is a classic run and gun action game heavily focused on boss battles. Inspired by cartoons of the 1930s, the visuals and audio are painstakingly created with the same techniques of the era, i.e. traditional hand drawn cel animation, watercolor backgrounds, and original jazz recordings. Play as Cuphead or Mugman (in single player or local co-op) as you traverse strange worlds, acquire new weapons, learn powerful super moves, and discover hidden secrets while you try to pay your debt back to the devil! ')  # noqa

session.add(game1)
session.commit()

game2 = Games(user_id=1,
              name='Dark Souls Remastered',
              catagory='Action',
              description='Then, there was fire. Re-experience the critically acclaimed, genre-defining game that started it all. Beautifully remastered, return to Lordran in stunning high-definition detail running at 60fps. Dark Souls Remastered includes the main game plus the Artorias of the Abyss DLC. ')  # noqa

session.add(game2)
session.commit()

game3 = Games(user_id=1,
              name='Far Cry Primal',
              catagory='Action',
              description='You will play as Takkar, a seasoned hunter and the last surviving member of your group. You have one goal: survival in a world where you are the prey. Grow your tribe and hone your skills to lead your people, conquer the land of Oros, and become the apex predator. Encounter a cast of memorable characters who can help push back the dangers of the wild. Face enemy tribes who will do anything to eradicate you and your allies.')  # noqa

session.add(game3)
session.commit()

game4 = Games(user_id=1,
              name='Middle-earth: Shadow of War ',
              catagory='Action',
              description='The sequel to the critically-acclaimed Middle-Earth: Shadow of Mordor-winner of over 50 industry awards-arrives the August, continuing the original story of Talion and Celebrimbor, who must now go behind enemy lines to forge an army and turn all of Mordor against the Dark Lord, Sauron.')  # noqa

session.add(game4)
session.commit()

game5 = Games(user_id=1,
              name='Batman: Return to Arkham',
              catagory='Action',
              description='Return to Arkham and experience two of the most critically acclaimed titles of the last generation - Batman: Arkham Asylum and Batman: Arkham City, with fully remastered and updated visuals. Batman: Return to Arkham includes the comprehensive versions of both games and includes all previously released additional content. ')  # noqa

session.add(game5)
session.commit()

# Fighting catagory and its initial items
catagory2 = Catagories(user_id=1, name='Fighting')

session.add(catagory2)
session.commit()

game1 = Games(user_id=1,
              name='Naruto Shippuuden Ultimate Ninja Storm 4',
              catagory='Fighting',
              description='With more than 12 million NARUTO SHIPPUDEN: Ultimate Ninja STORM games sold worldwide, this series established itself among the pinnacle of Anime & Manga adaptations to videogames! As every good story comes to an end, NARUTO SHIPPUDEN: Ultimate Ninja STORM 4 is going to be the most incredible STORM game released to date! Players around the world will experience the exhilarating adventures of Naruto Uzumaki like never before! The latest opus in the acclaimed STORM series will take gamers on a breathtaking and epic ride with new features like Change Leader System and Wall-run. For the first time ever, the world of NARUTO will also take advantage of the graphics power of the new generation systems. This is just the beginning and more characters and features will be announced in the future!')  # noqa

session.add(game1)
session.commit()

game2 = Games(user_id=1,
              name='Mortal Kombat XL',
              catagory='Fighting',
              description='One of the best-selling titles of 2015 has gone XL! Komplete The Mortal Kombat X Experience with new and existing content. Includes main game, and new playable characters Alien, Leatherface, Triborg, and Bo\'Rai Cho. Previously released playable characters include Predator, Jason Voorhees, Tremor, Tanya, and Goro. Also includes new skins pack Apocalypse Pack and all previously released skins packs. ')  # noqa

session.add(game2)
session.commit()

game3 = Games(user_id=1,
              name='Dragon Ball FighterZ',
              catagory='Fighting',
              description='After the success of the Xenoverse series, it\'s time to introduce a new classic 2D DRAGON BALL fighting game for this generation\'s consoles. DRAGON BALL FighterZ is born from what makes the DRAGON BALL series so loved and famous: endless spectacular fights with its allpowerful fighters. Partnering with Arc System Works, DRAGON BALL FighterZ maximizes high end Anime graphics and brings easy to learn but difficult to master fighting gameplay to audiences worldwide.')  # noqa

session.add(game3)
session.commit()

game4 = Games(user_id=1,
              name='Street Fighter 30th Anniversary Collection',
              catagory='Fighting',
              description='Celebrate the 30th Anniversary of the iconic Street Fighter franchise with the ultimate tribute to its arcade legacy in the Street Fighter 30th Anniversary Collection on PlayStation 4, Xbox One, Nintendo Switch and Windows PC in May 2018. This content-rich all-in-one package highlights the series\' past in an anthology of 12 classic titles with arcade-perfect balancing including the original Street Fighter, Street Fighter II, Street Fighter II: Champion Edition, Street Fighter II: Hyper Fighting, Super Street Fighter II, Super Street Fighter II: Turbo, Street Fighter Alpha, Street Fighter Alpha 2, Street Fighter Alpha 3, Street Fighter III, Street Fighter III: 2nd Impact and Street Fighter III: Third Strike. ')  # noqa

session.add(game4)
session.commit()

game5 = Games(user_id=1,
              name='Injustice 2',
              catagory='Fighting',
              description='Power up and build the ultimate version of your favorite DC legends in INJUSTICE 2. With a massive selection of DC Super Heroes and Super-Villains, INJUSTICE 2 allows you to equip every iconic character with unique and powerful gear earned throughout the game. Experience an unprecedented level of control over how your favorite characters look, how they fight, and how they develop across a huge variety of game modes. This is your super Hero. Your Journey. Your Injustice. ')  # noqa

session.add(game5)
session.commit()

# Role-Playing catagory and its initial items
catagory3 = Catagories(user_id=1, name='Role-Playing')

session.add(catagory3)
session.commit()

game1 = Games(user_id=1,
              name='The Elder Scrolls V: Skyrim Special Edition',
              catagory='Role-Playing',
              description='Winner of more than 200 Game of the Year Awards, Skyrim Special Edition brings the epic fantasy to life in stunning detail. The Special Edition includes the critically acclaimed game and add-ons with all-new features like remastered art and effects, volumetric god rays, dynamic depth of field, screen-space reflections, and more. Skyrim Special Edition also brings the power of PC mods to consoles. New quests, environments, characters, dialogue, armor, weapons and more - with Mods, the possibilities of what you can experience are nearly endless. ')  # noqa

session.add(game1)
session.commit()

game2 = Games(user_id=1,
              name='Diablo III Ultimate Evil Edition',
              catagory='Role-Playing',
              description='Face Ultimate Evil Over 13 million players have battled the demonic hordes of Diablo III. Now, it\'s your turn to join the crusade and take up arms against the enemies of the mortal realms. This Ultimate Evil Edition contains both Diablo III and the Reaper of Souls expansion set, together in one definitive volume. So stand ready. Something wicked this way comes.')  # noqa

session.add(game2)
session.commit()

game3 = Games(user_id=1,
              name='Fallout 4',
              catagory='Role-Playing',
              description='Bethesda Game Studios, the award-winning creators of Fallout 3 and The Elder Scrolls V: Skyrim, welcome you to the world of Fallout 4 - their most ambitious game ever, and the next generation of open-world gaming.')  # noqa

session.add(game3)
session.commit()

game4 = Games(user_id=1,
              name='The Witcher III: Wild Hunt',
              catagory='Role-Playing',
              description='Dedicated to gamers who want more from physical box editions of games than just the disc and manual, containing premium items prepared by the developers, this edition of The Witcher III: Wild Hunt is the definitive answer for those gamers who want to enter the Witcher Universe in style.')  # noqa

session.add(game4)
session.commit()

game5 = Games(user_id=1,
              name='Final Fantasy XV',
              catagory='Role-Playing',
              description='In a matter of days, the Kingdom of Lucis is to sign an armistice, ending a long and bitter conflict with Niflheim. Ahead of the ceremony, Prince Noctis, heir to the Lucian throne, sets forth from his homeland to formalize the union of states through his marriage to the Lady Lunafreya of the imperial province of Tenebrae. The offer of peace, however, is no more than a ruse to lower the Lucian shield, and the imperial army takes the crown city and its sacred crystal in one fell swoop. En route to his destination, Noctis is shocked to learn that he, his father the king, and his betrothed are believed dead. Overnight, the dream of peace has faded into a distant memory. His world crumbling around him, Noctis has naught but his resolve and his loyal companions to see him through the trials to come.')  # noqa

session.add(game5)
session.commit()

# Shooter catagory and its initial items
catagory4 = Catagories(user_id=1, name='Shooter')

session.add(catagory4)
session.commit()

game1 = Games(user_id=1,
              name='Red Dead Redemption',
              catagory='Shooter',
              description='Winner of over 100 Game of the Year awards including Spike Video Game Awards, Machinima Inside Gaming Awards, GameSpot, Games Radar, Spin, CNET, Associated Press and NY Post. America, 1911. The Wild West is dying. When federal agents threaten his family, former outlaw John Marston is forced to pick up his guns again and hunt down the gang of criminals he once called friends. Experience an epic fight for survival across the sprawling expanses of the American West and Mexico, as John Marston struggles to bury his bloodstained past, one man at a time.')  # noqa

session.add(game1)
session.commit()

game2 = Games(user_id=1,
              name='Wolfenstein II: The New Colossus',
              catagory='Shooter',
              description='Winner of Best Action Game at The Game Awards 2017, Wolfenstein II: The New Colossus is the highly anticipated sequel to the critically acclaimed first-person shooter, Wolfenstein: The New Order developed by the award-winning studio MachineGames.')  # noqa

session.add(game2)
session.commit()

game3 = Games(user_id=1,
              name='BioShock Infinite',
              catagory='Shooter',
              description='Indebted to the wrong people, and with his life on the line, hired gun Booker DeWitt has only one opportunity to wipe his slate clean. He must rescue Elizabeth, a mysterious girl imprisoned since childhood and locked up in the flying city of Columbia. Forced to trust one another, Booker and Elizabeth form a powerful bond during their daring escape. Together, they learn to harness an expanding arsenal of weapons and abilities, as they fight on zeppelins in the clouds, along high-speed Sky-Lines, and down in the streets of Columbia, all while surviving the threats of the air-city and uncovering its dark secret.')  # noqa

session.add(game3)
session.commit()

game4 = Games(user_id=1,
              name='Battlefield 1',
              catagory='Shooter',
              description='Experience the dawn of all-out war in Battlefield 1. Discover a world at war through an adventure-filled campaign, or join in epic team-based multiplayer battles with up to 64 players. Fight as infantry or take control of amazing vehicles on land, air and sea. And adapt your gameplay to the most dynamic battles in Battlefield history.')  # noqa

session.add(game4)
session.commit()

# Sports catagory and its initial items
catagory5 = Catagories(user_id=1, name='Sports')

session.add(catagory5)
session.commit()

game1 = Games(user_id=1,
              name='NBA 2K18',
              catagory='Sports',
              description='The future of sports career modes has arrived, allowing you to play the game the way you like. Build your career in NBA games, hit the courts in The Playground Park, join the Pro-Am circuit, or explore the shops and venues in an all-new open neighborhood setting. Featuring new MyPLAYER upgrade and endorsement systems, our biggest cast of characters to date including NBA players, and so much more.')  # noqa

session.add(game1)
session.commit()

game2 = Games(user_id=1,
              name='Madden NFL 18',
              catagory='Sports',
              description='This is Madden like you\'ve never seen it. Powered by the Frostbite engine, Madden NFL 18 introduces Longshot, a football redemption story you can play. Your decisions lead forgotten prospect, Devin Wade on the pursuit to fulfill his NFL dream in the first ever Madden story mode. Team up and dominate the gridiron with your friends in MUT Squads and play each matchup to your liking new Play Styles: Arcade, Simulation, and Competitive. Play the best real-world NFL matchups each week in Play Now Live! New stadium exteriors surrounded by vast cityscapes bring the spectacle of NFL gameday to life in the most photorealistic game to date.')  # noqa

session.add(game2)
session.commit()

game3 = Games(user_id=1,
              name='FIFA 18',
              catagory='Sports',
              description='Powered by Frostbite, EA SPORTS FIFA 18 blurs the line between the virtual and real worlds, bringing to life the players, teams, and atmospheres that immerse you in the emotion of The World\'s Game. The biggest step in gameplay innovation in franchise history, FIFA 18 introduces Real Player Motion Technology, an all-new animation system which unlocks a new level of responsiveness, and player personality - now Cristiano Ronaldo and other top players feel and move exactly like they do on the real pitch. Player Control combined with new Team Styles and Positioning give you the tools to deliver Dramatic Moments that ignite Immersive Atmospheres around the world.')  # noqa

session.add(game3)
session.commit()

game4 = Games(user_id=1,
              name='WWE 2K18',
              catagory='Sports',
              description='WWE fans, sports gamers, and fighting game fanatics - the biggest video game franchise in WWE history is back with WWE 2K18! With hard-hitting action, stunning graphics, drama, excitement, game modes, match types, creation capabilities, and everything you\'ve come to love from WWE 2K, WWE 2K18 promises to bring you closer to the ring than ever before. Be Like No One.')  # noqa

session.add(game4)
session.commit()
