
###############################################################################
#
# RecoverUsername
# Recovers a  username by triggering an email to a specified email address belonging to the user.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RecoverUsername(Choreography):

    """
    Create a new instance of the RecoverUsername Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OfficeDrop/RecoverUsername')


    def new_input_set(self):
        return RecoverUsernameInputSet()

    def _make_result_set(self, result, path):
        return RecoverUsernameResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RecoverUsernameChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RecoverUsername
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RecoverUsernameInputSet(InputSet):
        """
        Set the value of the Email input for this choreography. ((required, string) The email address associated with the username you want to recover.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)


"""
A ResultSet with methods tailored to the values returned by the RecoverUsername choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RecoverUsernameResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OfficeDrop.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RecoverUsernameChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RecoverUsernameResultSet(response, path)
