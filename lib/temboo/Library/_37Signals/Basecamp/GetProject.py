
###############################################################################
#
# GetProject
# Retrieves an individual project using a project id that you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetProject(Choreography):

    """
    Create a new instance of the GetProject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/GetProject')


    def new_input_set(self):
        return GetProjectInputSet()

    def _make_result_set(self, result, path):
        return GetProjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetProjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetProject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetProjectInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((string) The Basecamp account name for you or your company. This is the first part of your account URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Basecamp password.  You can use the value 'X' when specifying an API Key for the Username input.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ProjectId input for this choreography. ((integer) The ID for the project you want to retrieve.)
        """
        def set_ProjectId(self, value):
            InputSet._set_input(self, 'ProjectId', value)

        """
        Set the value of the Username input for this choreography. ((string) Your Basecamp username or API Key.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the GetProject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetProjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Basecamp.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetProjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetProjectResultSet(response, path)
