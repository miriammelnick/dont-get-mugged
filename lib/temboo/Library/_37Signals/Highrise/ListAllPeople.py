
###############################################################################
#
# ListAllPeople
# Retrieves contacts from your Highrise CRM.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListAllPeople(Choreography):

    """
    Create a new instance of the ListAllPeople Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Highrise/ListAllPeople')


    def new_input_set(self):
        return ListAllPeopleInputSet()

    def _make_result_set(self, result, path):
        return ListAllPeopleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListAllPeopleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListAllPeople
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListAllPeopleInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((string) The Highrise account name for you or your company. This is the first part of your account URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Highrise password. You can also use the value 'X' as a dummy password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((string) Your Highrise API Key)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the ListAllPeople choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListAllPeopleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Highrise.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListAllPeopleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListAllPeopleResultSet(response, path)
