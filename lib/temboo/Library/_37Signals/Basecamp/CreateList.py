
###############################################################################
#
# CreateList
# Creates a new To-do list for a specified project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateList(Choreography):

    """
    Create a new instance of the CreateList Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/CreateList')


    def new_input_set(self):
        return CreateListInputSet()

    def _make_result_set(self, result, path):
        return CreateListResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateListChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateList
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateListInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) The description of the list to create.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the MilestoneID input for this choreography. ((optional, integer) The ID of an existing milestone to include with the new list.)
        """
        def set_MilestoneID(self, value):
            InputSet._set_input(self, 'MilestoneID', value)

        """
        Set the value of the Name input for this choreography. ((optional, string) The name of the list to create.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the Password input for this choreography. ((string) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ProjectID input for this choreography. ((integer) The ID for the project in which you're creating the new list.)
        """
        def set_ProjectID(self, value):
            InputSet._set_input(self, 'ProjectID', value)

        """
        Set the value of the Username input for this choreography. ((string) A Basecamp account username or API Key.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the CreateList choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateListResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (No response is returned from Basecamp for update requests.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateListChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateListResultSet(response, path)
