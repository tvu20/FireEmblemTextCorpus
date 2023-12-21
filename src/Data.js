import React from "react";

import { GAMES_SO_FAR } from "./games";

const Data = () => {
  const url = (game) =>
    `https://github.com/tvu20/FireEmblemTextCorpus/tree/main/data/${game}`;

  const listGames = () => {
    return GAMES_SO_FAR.map((game) => {
      return (
        <li key={game}>
          <a href={url(game)} target="_blank" rel="noopener noreferrer">
            {game}
          </a>
        </li>
      );
    });
  };

  return (
    <>
      <h2>Data</h2>
      <h3>Folder Contents</h3>
      <ul>
        <li>
          Chapters folder: contains summary json files for each chapter in the
          game
        </li>
        <li>
          Speakers.json: summary information + counts about the speakers in the
          game
        </li>
        <li>
          speakers_cleaned.json: duplicated speakers file with nonimportant
          characters removed, with group and color information. used for
          cooccurence game
        </li>
        <li>
          cooccurrence.json: coocurence graph/matrix file, generated from
          speakers_cleaned.json
        </li>
        <li>Transitions.csv: dialogue transition counts in the game</li>
        <li>
          [gameid].csv: tagged csv file of all speaker dialogue lines, used for
          nlp
        </li>
        <li>full_transcript.txt: raw transcript of every chapter script</li>
        <li>
          full_transcript_cleaned.txt: removes tagged lines, punctuation,
          speakers
        </li>
        <li>words_summary.txt: words information (manually edited)</li>
        <li>words.txt: array of all words in game script</li>
        <li>
          phrases.txt: top 50 most commonly used phrases in the game script
        </li>
      </ul>
      {listGames()}
      {/* {url("FE1")} */}
      <h3>Sentiment Labels</h3>
      Options:
      <ul>
        <li>neutral</li>
        <li>joy</li>
        <li>sadness</li>
        <li>anger</li>
        <li>fear</li>
        <li>surprise</li>
      </ul>
      Some notes about labeling emotions:
      <ul>
        <li>
          joy includes statements with personal attachment, drive, fulfillment,
          agreement
        </li>
        <li>
          anger includes exclamatory statements with intent to harm or stand
          against someone
        </li>
        <li>
          fear includes statements with caution, initiating or pointing it out
        </li>
        <li>sadness includes being apologetic</li>
      </ul>
    </>
  );
};

export default Data;
