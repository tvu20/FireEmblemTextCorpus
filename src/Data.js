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
    </>
  );
};

export default Data;
