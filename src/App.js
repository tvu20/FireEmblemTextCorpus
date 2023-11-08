import React from "react";

import Inputs from "./Inputs";
import Data from "./Data";
import Scripts from "./Scripts";

import { GAMES_SO_FAR } from "./games";

const App = () => {
  const listGames = () => {
    return GAMES_SO_FAR.map((game) => {
      return (
        <li key={game}>
          {game} {game === "FE8" ? "(incomplete)" : ""}
        </li>
      );
    });
  };

  return (
    <>
      <h1>Fire Emblem Text Corpus</h1>
      <p>
        {" "}
        <a
          href="https://github.com/tvu20/FireEmblemTextCorpus/tree/main"
          target="_blank"
          rel="noopener noreferrer"
        >
          Github repository
        </a>
      </p>
      <p>
        <a
          href="https://drive.google.com/drive/folders/1brd7IVG5_6h45U_Ec6PyF75_QpoQPRtk?usp=sharing"
          target="_blank"
          rel="noopener noreferrer"
        >
          Drive link
        </a>
      </p>
      <p>
        <a
          href="https://docs.google.com/spreadsheets/d/1hLmguCeC3N8FLkww-vT_y9v7uY2Rh7y-GtZlOuyqjPY/edit?usp=sharing"
          target="_blank"
          rel="noopener noreferrer"
        >
          Resources spreadsheet
        </a>
      </p>

      <h2>Games so far:</h2>
      <ul>{listGames()}</ul>

      <Inputs />
      <Data />
      <Scripts />
    </>
  );
};

export default App;
