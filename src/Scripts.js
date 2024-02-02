import React from "react";

const Scripts = () => {
  return (
    <>
      <h2>Scripts</h2>
      <p>
        You can run the following scripts on all of the games by executing{" "}
        <i>runscripts.py</i>:
      </p>
      <li>
        <i>dialogue_parser_json.py</i>: goes through every chapter transcript
        for a given game and creates a chapter summary json file
      </li>
      <li>
        <i>text_data.py</i>: for each game, compiles every dialogue line into
        csv format
      </li>
      <li>
        <i>characters_list.py</i>: for each game, creates the speakers.json file
        using all the characters present in the transcripts
      </li>
      <li>
        <i>transitions.py</i>: for each game, creates transitions file
      </li>
      <li>
        <i>collect_chapters.py</i>: generate txt file with transcript for the
        entire game by collating information from each chapter transcript
      </li>
      <p>Other scripts:</p>
      <li>
        <i>randomizer.py</i>: randomize the lines in a text file
      </li>
      <li>
        <i>text_formatter</i> contains many formatting files for input
        collection
      </li>
      <li>
        <i>collect_multiple_speakers</i> generates full speaker file for games
        with multiple books
      </li>
      <li>
        <i>create_cooccurence.py</i> generates cooccurence file
      </li>
      <li>
        <i>words.py</i>: generates words data
      </li>
      <li>
        <i>gender/get_character_counts.py</i>: generates a list of characters
        for each gender per game
      </li>
      <li>
        <i>gender/get_gender_counts.py</i>: generates a list of line counts for
        each gender speaking per game
      </li>
      <li>
        <i>gender/combine_transitions.py</i>: combines transitions csv for
        subgroups of games
      </li>
      <li>
        <i>gender/get_transitions_json.py</i>: combines transitions csv for
        subgroups of games
      </li>
      <li>
        <i>social_networks/get_nodes.py</i>: generates a list of nodes based on
        character names
      </li>
      <li>
        <i>social_networks/get_links_list.py</i>: generates a list of links
        based on a list of pairings in the form person1, person2
      </li>
      <li>
        <i>social_networks/get_links_pairings.py</i>: generates a list of links
        representing different character pairings, including relationship tag
      </li>
      <h3>Prerequisites:</h3>
      <p>
        Every game must have a pre-made directory. In this directory must be a
        "chapters" folder. The game's directory in the input folder must also
        have a genders.json file (though this can be empty).
      </p>
    </>
  );
};

export default Scripts;
