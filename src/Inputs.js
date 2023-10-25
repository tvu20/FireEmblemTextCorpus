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
        <li>
          <a
            href="https://drive.google.com/drive/folders/1yqlml9m1Lzwq-Y_rjQ1BZ4oLJGKfCi_7"
            target="_blank"
            rel="noopener noreferrer"
          >
            Official release of Project Naga Script Repository
          </a>{" "}
          - compiled by reddit user Skelezomperman
        </li>
        <li>
          <a
            href="https://gamefaqs.gamespot.com/snes/577344-fire-emblem-thracia-776/faqs/43230"
            target="_blank"
            rel="noopener noreferrer"
          >
            FE5 transcript
          </a>{" "}
          (used for comparison)
        </li>
      </ul>
      <h3>Notes about transcripts</h3>
      <ul>
        <li>
          FE1-6 and FE12 are not localized, so I have compiled translations of
          their scripts. Characters are referred to by their localized names in{" "}
          <i>Fire Emblem Heroes</i> if possible.
        </li>
        <li>
          These transcripts assume that canon events occur - in particular,
          dialogue assumes that all playable characters are alive and recruited.
          If there are significantly different branching dialogues depending on
          someone's death, this is denoted by the branch path tags (explained
          below).
        </li>
        <li>
          For the FE4 transcripts, I assume that every female character from Gen
          1 was paired. If the replacement units have unique conversations then
          they are included; otherwise, I assume the person talking in the story
          is the original unit.
        </li>
        <li>
          For the FE7 transcripts, chapters are labeled according to Eliwood's
          route with combined dialogues from both routes. If a chapter is
          exclusive to Hector's route, "H" is included in the title.
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
          them
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
          around a map in or at the base
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
        <li>recruit-battle: %unit,boss</li>
      </ul>
      <h4>Titles</h4>
      <ul>
        <li>in character endings: #character-title</li>
        <li>in dialogue: #avatar-M represents male avatar</li>
        <li>in dialogue: #avatar-F represents female avatar</li>
      </ul>
      <p>Note about avatar tags - they reset on the next @ or % tag</p>
      <h4>Branching dialogue</h4>
      <ul>
        <li>
          ^start - indicates beginning of section with branching dialogue - only
          one possible per playthrough
        </li>
        <li>
          ^locked - indicates beginning of section that requires prerequisites
          to unlock
        </li>
        <li>^end - indicates end of branching section</li>
      </ul>
    </>
  );
};

export default Inputs;
