
###############################################################################
#
# DeletePeople
# Deletes a specified contact from your Highrise CRM.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeletePeople(Choreography):

    """
    Create a new instance of the DeletePeople Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Highrise/DeletePeople')


    def new_input_set(self):
        return DeletePeopleInputSet()

    def _make_result_set(self, result, path):
        return DeletePeopleResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeletePeopleChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeletePeople
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeletePeopleInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((string) The Highrise account name for you or your company. This is the first part of your account URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the ContactID input for this choreography. ((string) The ID number of the contact you want to delete. This is used to contruct the URL for the request.)
        """
        def set_ContactID(self, value):
            InputSet._set_input(self, 'ContactID', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Highrise password. You can also use the value 'X' as a dummy password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((string) Your Highrise API Key.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the DeletePeople choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeletePeopleResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Highrise. The delete people API method returns no XML, so this variable will contain no data.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeletePeopleChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeletePeopleResultSet(response, path)
