% Part B: Logic Programming (Prolog)
% Module Advisory and Certification

% --------------------------------------------------
% 1. FACTS
% --------------------------------------------------

learner(ali, computer_science).
learner(siti, information_technology).
learner(ahmad, computer_science).
learner(nur, information_technology).
learner(danial, software_engineering).

module(programming).
module(database).
module(web_development).
module(object_oriented_programming).
module(data_structures).
module(software_project).

completed(ali, programming).
completed(ali, database).
completed(ali, web_development).
completed(ali, object_oriented_programming).
completed(ali, data_structures).
completed(ali, software_project).

completed(siti, programming).
completed(siti, database).
completed(siti, web_development).

completed(ahmad, programming).
completed(ahmad, object_oriented_programming).

completed(nur, programming).
completed(nur, database).
completed(nur, object_oriented_programming).
completed(nur, data_structures).

completed(danial, programming).
completed(danial, database).

prerequisite(database, programming).
prerequisite(web_development, programming).
prerequisite(object_oriented_programming, programming).
prerequisite(data_structures, programming).
prerequisite(data_structures, object_oriented_programming).
prerequisite(software_project, programming).
prerequisite(software_project, database).
prerequisite(software_project, web_development).
prerequisite(software_project, object_oriented_programming).

required_module(programming).
required_module(database).
required_module(web_development).
required_module(object_oriented_programming).
required_module(data_structures).
required_module(software_project).

% --------------------------------------------------
% 2. RULES
% --------------------------------------------------

% A learner is eligible for a module when the learner and module exist,
% the module has not been completed, and all prerequisites are completed.
eligible(Learner, Module) :-
    learner(Learner, _),
    module(Module),
    \+ completed(Learner, Module),
    forall(
        prerequisite(Module, Req),
        completed(Learner, Req)
    ).

% Recommend modules which the learner is eligible to take.
recommended_module(Learner, Module) :-
    eligible(Learner, Module).

% Check whether a learner has completed a particular module.
certification_eligible(Learner, Module) :-
    completed(Learner, Module).

% Check whether a learner has completed every required module.
eligible_for_certification(Learner) :-
    learner(Learner, _),
    forall(
        required_module(M),
        completed(Learner, M)
    ).

% --------------------------------------------------
% 3. SAMPLE QUERIES AND RESULTS
% --------------------------------------------------

% Query 1: Successful eligibility
% ?- eligible(ahmad, database).
% true.

% Query 2: Unsuccessful eligibility
% ?- eligible(siti, data_structures).
% false.

% Query 3: Another eligibility case
% ?- eligible(danial, web_development).
% true.

% Query 4: Module recommendation
% ?- recommended_module(danial, M).
% M = web_development ;
% M = object_oriented_programming ;
% false.

% Query 5: Certification check - completed module
% ?- certification_eligible(ali, software_project).
% true.

% Query 6: Certification check - incomplete module
% ?- certification_eligible(siti, software_project).
% false.

% Query 7: Full certification eligibility
% ?- eligible_for_certification(ali).
% true.

% Query 8: Full certification eligibility
% ?- eligible_for_certification(siti).
% false.

