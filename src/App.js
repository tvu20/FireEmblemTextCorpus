import React from "react";

import Inputs from "./Inputs";
import Data from "./Data";
import Scripts from "./Scripts";

import { GAMES_SO_FAR } from "./games";

const App = () => {
  const listGames = () => {
    return GAMES_SO_FAR.map((game) => {
      return <li key={game}>{game}</li>;
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

      <h2>Games so far:</h2>
      <ul>{listGames()}</ul>

      <Inputs />
      <Data />
      <Scripts />
    </>
  );
};

export default App;
