

import logging

# ----------------- LOGGING SETUP -----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# ----------------- GUARDRAIL EXCEPTIONS -----------------
class InputGuardRailTripwireTriggered(Exception):
    pass

# ----------------- EXERCISE 1: Input Guardrail -----------------
def agent_input_guardrail(prompt):
    """
    Trigger InputGuardRailTripwire when certain text is detected in prompt.
    """
    logger.info(f"Agent received prompt: {prompt}")
    try:
        # Trigger condition
        if "😭" in prompt or "change my class" in prompt.lower():
            raise InputGuardRailTripwireTriggered("Input guardrail triggered!")
        logger.info("Prompt processed successfully.")
    except InputGuardRailTripwireTriggered as e:
        logger.warning(f"EXERCISE 1: {str(e)}")

# ----------------- EXERCISE 2: Father Guardrail -----------------
def father_guardrail(child_temperature):
    """
    Father prevents child from running outside below 26C.
    """
    logger.info(f"Child wants to run, temperature: {child_temperature}C")
    if child_temperature < 26:
        logger.warning("EXERCISE 2: Father says: 'You cannot run outside, too cold!'")
        return False
    logger.info("EXERCISE 2: Child can run safely.")
    return True

# ----------------- EXERCISE 3: Gate Keeper Guardrail -----------------
def gate_keeper_guardrail(student_school, allowed_school="OurSchool"):
    """
    Gate keeper prevents students of other schools from entering.
    """
    logger.info(f"Student school: {student_school}")
    if student_school != allowed_school:
        logger.warning("EXERCISE 3: Gate keeper says: 'Access denied for outside students!'")
        return False
    logger.info("EXERCISE 3: Access granted.")
    return True

# ----------------- MAIN -----------------
if __name__ == "__main__":
    # Exercise 1
    agent_input_guardrail("I want to change my class timings 😭😭")

    # Exercise 2
    father_guardrail(24)  # Below 26C
    father_guardrail(28)  # Above 26C

    # Exercise 3
    gate_keeper_guardrail("OtherSchool")  # Blocked
    gate_keeper_guardrail("OurSchool")    # Allowed





