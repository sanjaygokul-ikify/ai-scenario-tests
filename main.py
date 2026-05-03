import json
import os
from src.test_scenario import TestScenario
from src.ai_agent import AiAgent
from src.test_evaluator import TestEvaluator
from src.test_reporter import TestReporter
def main():
    scenario_file = 'example_scenario.json'
    with open(scenario_file, 'r') as f:
        scenario_data = json.load(f)
    scenario = TestScenario(scenario_data)
    agent = AiAgent()
    evaluator = TestEvaluator()
    reporter = TestReporter()
    result = evaluator.evaluate(agent, scenario)
    reporter.report(result)
if __name__ == '__main__':
    main()