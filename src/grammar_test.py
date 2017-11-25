from grammar import SimpleGrammar

sg = SimpleGrammar()
sg.add_tag("story", ["#story_beginning# #story_problem# #story_climax# #story_ending#"])
sg.add_tag("story_beginning", ["Once upon a time there was a valiant #animal#"])
sg.add_tag("story_problem", ["that never #difficulty_verb#.", \
            "that one day heard some strange words: #strange_calling#"])
sg.add_tag("story_climax", ["Suddenly, he decided to #resolution_verb#."])
sg.add_tag("story_ending", ["Finally he could #result_verb# without worries."])
sg.add_tag("difficulty_verb", ["slept", "danced", "talked"])
sg.add_tag("resolution_verb", ["run", "sing", "give up"])
sg.add_tag("result_verb", ["sleep", "dance", "talk freely"])
sg.add_tag("strange_calling", ["Hello #name#!", "Hello my #writer_object#!"])
sg.add_tag("animal", ["dolphin", "dog", "cat", "lamb", "lion"])
sg.add_tag("name", ["Mr. Gil", "Madame", "Masked Man"])
sg.add_tag("writer_object", ["text", "book", "beloved code"])

print(sg.evaluate("#story#"))