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
        <li>Transitions.csv: dialogue transition counts in the game</li>
      </ul>
      {listGames()}
      {/* {url("FE1")} */}
    </>
  );
};

export default Data;
