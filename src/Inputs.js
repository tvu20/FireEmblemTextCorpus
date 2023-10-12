import React from "react";

const Inputs = () => {
  return (
    <>
      <a
        href="https://github.com/tvu20/FireEmblemTextCorpus/tree/main/input"
        target="_blank"
        rel="noopener noreferrer"
      >
        <h2>Inputs (Raw Data)</h2>
      </a>
      <p>
        Contains transcripts and character information scraped from the
        following sites:
      </p>
      <ul>
        <li>
          <a
            href="https://fireemblemwiki.org/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Fire Emblem Wiki
          </a>
        </li>
        <li>
          <a
            href="https://fireemblem.fandom.com/wiki/Fire_Emblem_Wiki"
            target="_blank"
            rel="noopener noreferrer"
          >
            Fire Emblem Fandom Wiki
          </a>
        </li>
        <li>
          <a
            href="https://serenesforest.net/"
            target="_blank"
            rel="noopener noreferrer"
          >
            Serenes Forest
          </a>
        </li>
        <li>
          <a
            href="https://wiki.serenesforest.net/index.php/Main_Page"
            target="_blank"
            rel="noopener noreferrer"
          >
            Serenes Forest Wiki
          </a>
        </li>
      </ul>
      <h3>Guide to transcript text files:</h3>
      <h4>Main tags</h4>
      <ul>
        <li>@Opening: Opening narration for a chapter</li>
        <li>@Intro: Dialogue before chapter begins</li>
        <li>
          @Battle: Dialogue during the battle that player will encounter
          naturally
        </li>
        <li>@End: Dialogue after battle ends</li>
        <li>@Visit: Dialogue that plays when you visit a village</li>
        <li>@Flashback: Dialogue flashback outside of battle</li>
        <li>
          @Recruit-Visit: Dialogue if you visit a village to recruit someone
        </li>
        <li>@Boss: Dialogue that plays when you fight a boss</li>
        <li>
          @Recruit-Battle: Dialogue if you fight someone you can recruit during
          battle
        </li>
        <li>@Character-Falls: Plays if your unit dies in battle</li>
        <li>
          @Recruit-Talk: Dialogue if you talk to someone you can recruit during
          battle
        </li>
        <li>
          @Battle-Talk: Dialogue if two of your units talk during a battle
        </li>
        <li>
          @Boss-Talk: Dialogue if you talk to a chapter boss outside of fighting
          tehm
        </li>
        <li>
          @Narration: Narration that doesn't occur within an opening of a
          chapter
        </li>
        <li>
          @Dialogue: Story-relevant dialogue scenes not tied to a particular
          battle
        </li>
        <li>
          @Conversation: Talking to people in the world in games you can run
          around a map in
        </li>
        <li>
          @Recruit-Conversation: Recruiting someone by talking to them in the
          world
        </li>
        <li>@Cutscene: anime cutscene dialogue</li>
      </ul>
      <h4>Sub tags</h4>
      <p>
        Used to specify which units are involved in a conversation. Format:
        unit1,unit2
      </p>
      <ul>
        <li>recruit-talk: %recruiter,recruit</li>
        <li>battle-talk: %person1,person2</li>
        <li>boss: %unit,boss</li>
        <li>boss-talk: %unit,boss</li>
      </ul>
      <h4>Titles</h4>
      <ul>
        <li>in character endings: #character-title</li>
        <li>in dialogue: #avatar-M represents male avatar</li>
        <li>in dialogue: #avatar-F represents female avatar</li>
      </ul>
      <p>Note about avatar tags - they reset on the next @ or % tag</p>
    </>
  );
};

export default Inputs;
