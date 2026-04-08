---
title: "Ai Workflows"
date: 2026-04-07T00:00:00-08:00
lastmod: 2026-04-07T00:00:00-08:00
author: Alexander Saavedra
tags: [ai, software]
draft: true
enableDisqus: true
enableMathJax: false
math: false  # set to true to load KaTeX on this page
disableToC: false
disableAutoCollapse: true
---


All standard [disclaimers](/disclaimers/) apply to this post.

# Introduction
The role of the human in software is shifting from writer to orchestrator and judge. 
As AI agents scale from autocomplete to autonomous fleets, the question is 
no longer whether to use them but how to wield them without losing control. 
This article covers where we are, what still matters, and how to build workflows that actually work.

## Levels of AI Adoption

Where are you?

| Level | Name | Description | Era |
|-------|------|-------------|-----|
| **L1** | No AI | Traditional dev workflow, no AI tooling. | IDE Era |
| **L2** | Agent in IDE, permissions on | You approve every file change, full manual control. | IDE Era |
| **L3** | YOLO mode | Agent runs freely in IDE, trust is rising. | IDE Era |
| **L4** | Diffs fade, conversation leads | You stop reviewing every diff, you watch what the agent is doing and focus on guiding it. | Agent-First |
| **L5** | Agent-first, IDE later | You work in the agent conversation, the IDE is just where you look at the code afterward. | Agent-First |
| **L6** | Agent multiplexing | Bored waiting? Fire up another agent. Then another. You're bouncing between streams and you can't stop. | Agent-First |
| **L7** | 10+ agents, managed by hand | "Oh gosh, I've made a mess." Wrong context sent to the wrong agent. You start asking: "What if Claude Code could run Claude Code?" | Orchestration |
| **L8** | Build your own orchestrator | You write the coordination layer yourself, spawning, routing, and managing agents programmatically. | Orchestration |
| **L9** | The Honey Bee Hive | A fully autonomous, self-managed repository. Agents execute goals independently — you only check in to harvest the output. | Orchestration |
| **L10** | Human taste tester | Still being built out, but a one person fully agentic full swarm shop https://theinnermostloop.substack.com/p/the-first-one-person-ai-conglomerates | Conductor |

L9 and L10 admittedly could have better names but I can change that later. 
As you reach these final levels you'll be more of a "bee factory builder" 
or "bee maintainer" than much of anything else.

[Levels of Ai Adoption](https://x.com/garrytan/status/2033623617448091809?s=20)

## Three Major Classes of Programmers in 2026

- **Traditionalists**: Programmers who avoid LLMs and write code manually from scratch.
- **Hybrids**: Programmers who still design the system themselves but use AI heavily to help 
  generate code; Andrej Karpathy places himself in this group.
- **Agentic Developers**: Programmers who rely on autonomous AI agents to generate and build products end to end.

For this article we're going to focus on the cutting edge of what's going on
in the field and where the human fits into this process.

![Human-centered swarm intelligence](/ai-workflows/0-human-centered-swarm-intelligence.webp)

## What won’t change
The primitives of the software development lifecycle will remain the same.
You still need to gather requirements, define acceptance criteria, design systems, 
write tests, review outputs, and deploy with confidence. None of that goes away 
just because an agent wrote the code instead of you.

The need for sensors and ground truth data remains. Effectively humans will act
as ground truth sensors and judgement detectors on numerous levels. Someone has to 
decide whether the output is correct, whether the abstraction is right, whether the 
test actually tests the thing that matters. That someone is still you.

You should always start off your process with as few assistants as possible. 
Add agents only when you can verify their output and understand their failure modes.

## Ai for writing and coding
![Target specificity](/ai-workflows/Target-specifity.webp)

I start my outline and process for writing articles this way, obviously this is 
idealized to some degree:

1. I have pencil and paper
2. I move onto writing it all down using vim with no autocomplete
3. I proofread myself or just read it for clarity and precision.
4. I get an Ai to lightly spell check or give feedback paragraph by paragraph
5. Get an Ai to play the role of a counter arguer or find areas of weakness 
in my perspective. 
6. If possible, I get the most well seasoned person I know in a given area 
who can provide effective feedback with a well refined prompt for what 
I am looking for in terms of their editing and reviewing of my work.
7. Usually, I can't get this, but get an team of rivals. A consortium of the 
best thinkers and doers to battle test your ideas and test the work for 
prime time.

You still need a team of rivals and varying viewpoints to struggle against. 
Viewpoint diversity matters a lot still. 
There was even a book written on this topic: https://en.wikipedia.org/wiki/Team_of_Rivals. 

## Ai for Coding

![Gap in formal verification](/ai-workflows/gap-formal-verification.webp)
Credit to Evan Miyazono for the image above.

1. I write out in vim or use pencil and paper and go through the draft 
of what I'm looking to build and what the structure of what I'm building. 

In essence, I am distilling the intent of what I am trying to achieve, not necessarily
the best approach. Remember, these things can search the implementation space 
potentially more effectively than you in certain cases so I am sometimes implementation agnostic.

The question to be answered is: **What's the minimal viable context to give Ai 
to perform this task?**

Make sure to generate lots of ideas or strategies to achieve goals.

Good strategy can be defined by these elements: 
  
  1. Diagnosis to define the challenge by why you are doing this.

  2. Guiding policy for dealing with the challenge of what is being done.
  
  3. Coherent set of actions to implement the guiding policy by figuring out how you will make it happen.

Bad strategy avoid tradeoffs that are critical and unavoidable while not having
a clear and well defined implementation roadmap laid out. Strategies are 
highly detailed, able to decompose everything and anything that needs to be 
broken down further when needed, and have clear objectives that directly map
back to the overarching goal.

These definitions were inspired and clarified by the book Good Strategy, Bad Strategy 
by Richard Rumelt.

2. I consider a well defined target that I'm trying to reach with this project or code.

  a. What does a success condition look like? These systems are excellent at gaming 
their reward functions which is the Ai equivalent of the monkey paw. 
  b. They'll do what you say but the spirit of the word is lost, meaning the intent 
has been lost, in the instructions.
  c. Brainstorm possible paths and strategies to achieve these ideas. Provide your 
  own as a baseline and let them add to this list. Make sure to remove ones you
  don't want or aren't correct. 

Question to be answered: **What's the most precise  target to set as a reward and 
verify the task has been complete?**

3. Now I start writing what types of tests, behaviors, and strategies should
exist to verify at every level the goal is complete.

  a. Could it be done more efficiently? 
  b. Could it be done more effectively? 
  c. Lots of ideation and brainstorming takes place here. 

# What will change

The ability for agents and humans to coordinate will continue to scale more over time. 
This means high agency individuals will have further reach than ever before. 
Solofounders will no longer be a pipe dream--some people will indeed be the primary 
orchestrator of a fleet of agents. A single developer can now scaffold a full-stack 
application, write its test suite, and deploy it in a day. A small team can do what 
used to require a department.

The economy will further bisect between the high and low agency at a rate and speed 
never seen before. Those who can precisely define intent, set clear targets, and 
verify outputs will compound their leverage. Those who cannot will find their work 
increasingly automatable. The skill that matters most is no longer writing code--it's 
knowing what to build, why, and how to verify it was built correctly.

# High Leverage Things
Things that will have more leverage now more than ever: 

0. **Deep and sustained focus**: I have previously written for numerous years about deep work, productivity, and 
other aspects of this but it is now more critical than ever since the distraction 
economy is stronger than ever. Social media, and its crack cocaine cousin shorts 
and micro-form content are making us glibber and less effective for our actual goals.
Your brain is being hijacked and turned into a slot machine. 
Get comfortable with boredom, actually make sure it’s both frequent and welcomed. Boredom is where original thought comes from.

1. **Taste**: in both the aesthetic and design sense. Knowing the right thing to build for the right time will become invaluable.

2. **High Agency**: Things like clear thinking, bias to action, critically and effectively questioning authority (disagreeability) are strong signs of high agency. 
Expanded upon this idea in the additional resources section.

3. **Reasoning and empiricist mindset**: what I cannot create, I cannot understand. 
You should be able to build, deploy, and explain every part of the stack in which you’re working. 

One book on this topic is 
The Irrational Decision: How We Gave Computers the Power to Choose for Us by Ben Recht

In short, you still need to be able to weigh decisions outside of the purely 
calculation based quantatitive framework

> “Not everything that counts can be counted and not everything than can be counted counts.”
― Albert Einstein supposedly had this quote nailed up in his office

I write this because a fair amount of people I deal with who are
[current modelers](/posts/models/#precurrentpost-modelers) are just **current modelers**
who think mathematical and statistical descriptions of the world are the territory
not the map. Meaning the representation of reality IS INDEED reality. This is 
a fallacy of course.

4. Artisanship: If you look at true artisans like Jiro, Phil Tippett, 
Ursula Le Guin, or others, they delved deep into the inner sanctum to 
produce massive works of genius and quality, understanding every detail of their 
craft.  
Quality and taste take time, it requires deliberate and sustained learning over a 
period of time. The more deliberate and intense the shorter the time but there are limits here. 
Steven Jobs: the internal and external structure of the products was beautiful, why?
A hidden and paradoxical point within capital markets is that altruistic 
obsession with quality and perfection can outcompete a company just following profit motives.
**Markets require an irrational sustained commitment to craft.**

In the long run the market is a weighing machine, not a voting machine as 
Benjamin Graham of the Intelligent Investor said. To get the weight on your
side your connection with your craft has to run deep and broad.

GI Joe Fallacy - Knowing is not half the battle. Knowing and doing are worlds 
apart and ultra high agency will become even more valuable. 
Tyler Cowen, who I've quoted before in his book Average is Over, understands
that the gap will grow between those with high agency and those without.

https://www.highagency.com/ is a great resource for thinking about this topic. 

# Documentations and Decisions

**Minimum**: you need to understand the code and the side effects of it. 

**Better**: if you got hit by a bus others can understand it

**Best**: If you got hit by a bus that person and agents can understand both how and why you made your decisions. What evidence you considered, what tradeoffs were made, and why things are the way they are. The best case is more of a direction and not a destination. The other two can easily be reached. 

Remember this “when there is doubt, log it out.” and 
“when in distress, write a test.” It’s silly but it works effectively to make 
sure you’re taking an empirical approach at every step  of the process.

# Ai Assisted Engineering

![Spectrum: vibe coding vs engineering](/ai-workflows/4-spectrum-vibe-vs-engineering.webp)

There is a spectrum between vibe coding and rigorous engineering. The core principle 
is the same regardless of where you sit on it: limit variables, minimize non-deterministic 
processes, and minimize unwanted side effects. All the standards and tools of engineering 
still apply, just way faster. 

The question is what breaks when you try to go from prototype to production. 
That's the 70 percent problem:

![The 70 percent problem](/ai-workflows/70-percent-problem.webp)

Ai can get you the boilerplate, basic testing, and a working prototype. But it cannot 
get you to a scaled industrial-grade application on its own. This will change with 
time but right now you need several pieces to bridge the gap. Here are the ones 
I've found most critical:

**1. Deterministic scaffolding.** Your agents need a backbone that doesn't hallucinate.

![Bash scripting as connective tissue](/ai-workflows/bash-scripting-connective-tissue.webp)

Bash scripts, Makefiles, CI pipelines--these are the deterministic skeleton that holds 
your agentic workflow together. The agent generates code; the scaffold builds, tests, 
and deploys it. Never let the non-deterministic part control the control flow.

**2. The right mental model for LLMs.**

![Ghost LLM mental model](/ai-workflows/ghost-llm-mental-model.webp)

As the context window fills, the model's reading comprehension degrades. This is why 
minimal viable context for tasks matters--and why setting a precise target up front 
is not optional. Treat the context window as a scarce resource, not an infinite notepad.

**3. You still have to think.**

![No substitute for thinking](/ai-workflows/No-substitute-for-thinking.webp)

There is no substitute for thinking thoroughly and deeply yourself. The agent 
accelerates execution, not judgment. If you don't understand the problem, 
the agent will confidently build the wrong thing faster.

**4. Clear targets are non-negotiable.**

![Target setting](/ai-workflows/target-setting.webp)

You must set clear and well defined targets, otherwise your outputs will be 
poorly structured. Garbage targets, garbage results. This applies to every level: 
the project goal, the task description, and the individual prompt.

**5. Some things still require a human hand.**

![Blinds](/ai-workflows/blinds.gif)

Certain things will still need to be hand crafted or done.
I have found this especially true for generating images, I still use low level 
design tools frequently. Know where the boundary is between what the agent can 
do well and where you need to step in.

**6. Your knowledge is the bottleneck, not your prompting.**

![Education vs prompt quality](/ai-workflows/2-claude-education-vs-prompt-quality.webp)

What you know matters a lot, this is true now more than ever. I don't think
just years of education are the be all and end all, but you must develop
strong and hard earned skills to stay relevant. You cannot vibe your way 
into expertise, deep knowledge, and profound insight. The quality of what you 
can build with AI is bounded by what you can recognize as correct or incorrect.

https://thisistheway.to/ai/primitives/
The framework defines AI primitives as the fundamental building blocks required 
to transition from simple chat interfaces to sophisticated, autonomous agents. 
These five core components are Intelligence, Context, Logic, Loop, and Output, 
each serving a specific role in a functional AI system. 
Intelligence acts as the central LLM engine, while Context provides the necessary memory 
or data retrieval to ensure the model remains grounded and relevant. Logic empowers 
the AI to interact with the physical or digital world through tool use and code execution. 
The Loop primitive introduces self-reflection and iteration, allowing the system to refine 
its answers and complete multi-step tasks. Finally, Output focuses on the structural 
formatting or the specific actions that conclude the AI's workflow.

[You need agents able to use multiple models to have a consortium of experts](https://x.com/burkeholland/status/2019856950461104220)

Note: there are lots of tips and tricks that are constantly covered online
and most are them are silly or mildly useful for awhile. 
The high level pieces are try to make sure to keep the right context, skills,
and efficiency everytime you do things.
As you continue on this path you'll realize tactics come and go, but strategy remains.

# Cognitive Enhancements and Decision Frameworks

![Eisenhower matrix: crawl, walk, run agents](/ai-workflows/1-eisenhower-matrix-crawl-walk-run-agents.webp)

> “He was fascinated by the idea of human and machine inextricably bound to each other, each testing the limits of the other.” ~ Chapterhouse Dune

The eisenhower matrix applies in the age of Ai more than ever, we can delegate a lot 
of tasks effectively now more than ever but these should be done deliberately.
Automating a stupid task is just stupidity repeated more.
The crawl, walk, run framework is whether you're the primary driver, mutual, or 
your Ai agent is the primary driver respectively.



> “There’s a lesson in that too. What do such machines really do? They increase the number of things we can do without thinking. Things we do without thinking, there’s the real danger.” 
~ God Emperor of Dune

Note: this story may be fictitious but it's irrelevant to the fact that the workflow 
is the point I'm getting at. A story does not need to be actually true to be illustrative
of the point.

Here's the workflow his advisor called "the most sophisticated research process 
I've seen in 20 years." He starts every essay with a brutal diagnostic prompt. 
Dumps his rough argument into Claude and asks: 
> "What are the 3 weakest logical jumps in this reasoning? Where would a hostile examiner attack first?" 
The AI doesn't write his essay. It destroys his draft. Then he rebuilds. But 
the next step is what separates him from every other student using ChatGPT or 
Claude to generate paragraphs. He uploads the top 5 papers in his field and asks: 

> "What claims in my argument contradict or oversimplify what these authors actually found?" 

Most students cite papers they've skimmed. He cites papers he's been forced to genuinely understand. The final move is almost unfair. 

Before submitting, he pastes his conclusion and asks: 
> "What would a philosopher of science say is missing from this argument? What assumptions am I making that I haven't defended?"

His essays come back with comments like "unusually rigorous" and "demonstrates rare critical depth." He's not using AI to write. He's using it to think harder than he could alone. The tool hasn't changed. The workflow has.”

[Using Ai to think harder and more effectively](https://x.com/ihtesham2005/status/2033152573033914722?s=20)

[Tiago Forte’s](https://www.buildingasecondbrain.com/para) perspective of Ai tools as a superpowered exoskeleton is a powerful one.
Additionally, using more complex knowledge management systems like PARA (Tiago Forte’s system) or others software tools like Obsidian can be powerful strategies to setup and navigate your knowledge. This also includes gaps in your reasoning, gaps in knowledge, and workflow gaps to name a few.
Projects - actively being worked on
Areas - roles and responsibilities you're managing over time
Resources - topics you're interested in that could be useful in the future
Archives - complete or inactive items from the other three categories


## Knowledge management system tools

```https://www.reddit.com/r/ClaudeAI/comments/1qr19df/claude_code_obsidian_how_i_use_it_short_guide/```
Note: Claude is just one LLM tool and you can definitely user others. This article is just the most comprehensive of the concept I am getting at.I definitely would highly recommend creating the automation and test harness using an AI tool if you’re not familiar with these systems but the question of whether you should allow this tools to gain access to your most valuable data is a personal choice.The essential goal is “write once, surface anywhere.” so all knowledge you have is at your fingertips.

For the more technical folks I’d recommend using these tools with command line 
interfaces more in depth like short cut keys, integration with other tools, and things like automated 
saves, pushes, deployments, like you would a software codebase in general. 

# Conclusions

I recommend using these tools, thinking about them deeply, and adapting all of these workflows for your use cases.
The swarm is here and to be at the heart of the swarm requires incredibly sophisticated and coherent workflows at every level.
It’s a strange and new world for some. For others, it’s just another Thursday as SciFi scenarios become science fact, and then finally mundane.
If you’re still skeptical, then I will simply quote my favorite grumpy investor
“Sir--I gave you an argument, I cannot give you an understanding." ~ Samuel Johnson,
Or said an even more immodest way:
“You will come around because I am right and you’re smart."  ~ Charlie Munger


## Additional Resources

Two books I used to cover these topics thoroughly are:
  1. Vibe Coding by Steve Yegge
  2. Beyond Vibe Coding by Addy Osmani

Only tip I'm going to give: get the Ai to try to use caveman talk to simplified response 
language so it compresses it's responses and what it does. It works.

[how to use claude code according to Boris Cherny](https://x.com/bcherny/status/2017742741636321619)
https://link.springer.com/chapter/10.1007/978-1-4612-5695-3_22 

[What happens to developers in the future? I don’t know. My intuition says they don’t go away](https://youtube.com/shorts/3tWRq1Dv1as?si=UqddNOhuzeIxh8tU)

https://haskellforall.com/2026/03/a-sufficiently-detailed-spec-is-code

https://blog.cosmos-institute.org/p/the-last-temptation-of-claude?r=1ds20&utm_medium=ios&triedRedirect=true 

Chaos Engineering and other types of stress testing are still conceptually valid strategies. The concept of the simian army, Netflix's chaos monkeys, is still a useful idea for testing things out but we’ve moved beyond this model now: https://news.ycombinator.com/item?id=46464953 

[The Humble Programmer by Dijkstra](https://www.cs.utexas.edu/~EWD/transcriptions/EWD03xx/EWD340.html)

https://www.oneusefulthing.org/ 

https://howborisusesclaudecode.com/

https://www.businessinsider.com/amazon-tightens-code-controls-after-outages-including-one-ai-2026-3

[Scaling long-running autonomous coding](https://cursor.com/blog/scaling-agents)

https://www.modular.com/blog/the-claude-c-compiler-what-it-reveals-about-the-future-of-software

https://open.spotify.com/episode/0Va0tXyRPwicecz1aMg3vT?si=E1tww2H1TA-d-flosg-JvA&t=3180&pi=mqcL6NyyRjqJ4 

key line 
> “here is a piece of code no one understands. Am I willing to bet my whole company's product on it? I don’t know…I don’t know what to do now.” 
This talks about the ever present pernicious loss of control when using Ai tools.

[jeremy howard on coding vs software engineering](https://share.solve.it.com/d/28d1864aad0723170e76fc4f720058c8)


https://youtu.be/eA9Zf2-qYYM?si=cYOi7TYq_Whn6xk4 
https://steipete.me/posts 

[Programming in an underrgaduate CS curriculum by Bjarne Stroustrup](https://www.stroustrup.com/software.pdf)
The summary of this article by Dr.Stroustrup is that Computer Science was always a 
hodge podge of subjects awkwardly placed together with little coherence. 
The fact that the undergraduate CS major is dying, in my view not his, is probably 
good because it was a stupid amalgamation of stuff.

The tension at the other end is to the Dune quotes referenced above is: 
> “Civilization advances by extending the number of important operations which 
> we can perform without thinking of them.” 
~ Alfred North Whitehead

https://open.spotify.com/episode/0Va0tXyRPwicecz1aMg3vT?si=OzdePXHgQKeoCZ-n2WQbhQ&t=3062&pi=EnDrvCwGQiGjd this is by far the best argument against this vibe coding crap culture going on. Opinions my own, but it annoys me how companies who vibe feature build are legitimately destabilizing their products.


```
## Workflow Orchestration

### 1. Plan Node Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately - don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One tack per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from the user: update `tasks/lessons.md' with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Belanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes - don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests - then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Task Management

1. ** Plan First **: Write plan to `tasks/todo.md' with checkable items
2. ** Verify Plan **: Check in before starting implementation
3. ** Track Progress **: Mark items complete as you go
4. ** Explain Changes **: High-level summary at each step
5. ** Document Results **: Add review section to 'tasks/todo.md
6. ** Capture Lessons **: Update `tasks/lessons.md' after corrections

## Core Principles

- ** Simplicity First **: Make every change as simple as possible. Impact minimal code.
- ** No Laziness **: Find root causes. No temporary fixes. Senior developer standards.
- ** Minimal Impact **: Changes should only touch what's necessary. Avoid introducing bugs.
```
https://x.com/Hartdrawss/status/2026590665304391963?s=20 

[Ai Code tips that have made my life easier:](https://x.com/svpino/status/2018682144361734368?s=20)
```(Add these to your [ai tool].md file)
1. "Before writing any code, describe your approach and wait for approval. Always ask clarifying questions before writing any code if requirements are ambiguous."
2. "If a task requires changes to more than 3 files, stop and break it into smaller tasks first."
3. "After writing code, list what could break and suggest tests to cover it."
4. "When there’s a bug, start by writing a test that reproduces it, then fix it until the test passes."
5. "Every time I correct you, add a new rule to the CLAUDE .md file so it never happens again."
```

