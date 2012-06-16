
###############################################################################
#
# PasswordCriteria
# Verifies that a given password matches a standard pattern for passwords.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PasswordCriteria(Choreography):

    """
    Create a new instance of the PasswordCriteria Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Temboo/Validation/PasswordCriteria')


    def new_input_set(self):
        return PasswordCriteriaInputSet()

    def _make_result_set(self, result, path):
        return PasswordCriteriaResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PasswordCriteriaChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PasswordCriteria
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PasswordCriteriaInputSet(InputSet):
        """
        Set the value of the MaxLength input for this choreography. ((optional, integer) The max length you want to allow for the password. Defaults to 14.)
        """
        def set_MaxLength(self, value):
            InputSet._set_input(self, 'MaxLength', value)

        """
        Set the value of the MinLength input for this choreography. ((optional, integer) The minimum length you want to allow for the password. Defaults to 6.)
        """
        def set_MinLength(self, value):
            InputSet._set_input(self, 'MinLength', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The password to validate.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)


"""
A ResultSet with methods tailored to the values returned by the PasswordCriteria choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PasswordCriteriaResultSet(ResultSet):
        """
        Retrieve the value for the "Match" output from this choreography execution. ((string) Contains a string indicating the result of the match -- "valid" or "invalid".)
        """
        def get_Match(self):
            return self._output.get('Match', None)

class PasswordCriteriaChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PasswordCriteriaResultSet(response, path)
