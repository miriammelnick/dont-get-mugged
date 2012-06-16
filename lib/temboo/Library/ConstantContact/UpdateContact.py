
###############################################################################
#
# UpdateContact
# Updates an existing contact in your Constant Contact system when you supply a contact ID to the Choreo.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateContact(Choreography):

    """
    Create a new instance of the UpdateContact Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ConstantContact/UpdateContact')


    def new_input_set(self):
        return UpdateContactInputSet()

    def _make_result_set(self, result, path):
        return UpdateContactResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateContactChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateContact
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateContactInputSet(InputSet):
        """
        Set the value of the UpdatedContactXML input for this choreography. ((XML) This input should be the updated XML returned from a GET contact method.)
        """
        def set_UpdatedContactXML(self, value):
            InputSet._set_input(self, 'UpdatedContactXML', value)

        """
        Set the value of the APIKey input for this choreography. ((string) API Key provided by Constant Contact)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ContactId input for this choreography. ((integer) The id for the contact you want to update)
        """
        def set_ContactId(self, value):
            InputSet._set_input(self, 'ContactId', value)

        """
        Set the value of the ListId input for this choreography. ((integer) The ID for the list that you want to update)
        """
        def set_ListId(self, value):
            InputSet._set_input(self, 'ListId', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Constant Contact password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the UserName input for this choreography. ((string) You Constant Contact username)
        """
        def set_UserName(self, value):
            InputSet._set_input(self, 'UserName', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateContact choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateContactResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The both responses from Constant Contact. Note that a successful update returns no content.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class UpdateContactChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateContactResultSet(response, path)
