
###############################################################################
#
# ObtainContactInformation
# Retrieves contact information from Constant Contact by specifying the contact ID.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ObtainContactInformation(Choreography):

    """
    Create a new instance of the ObtainContactInformation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ConstantContact/ObtainContactInformation')


    def new_input_set(self):
        return ObtainContactInformationInputSet()

    def _make_result_set(self, result, path):
        return ObtainContactInformationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ObtainContactInformationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ObtainContactInformation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ObtainContactInformationInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((string) API Key provided by Constant Contact)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ContactId input for this choreography. ((integer) The ID for the contact you want to retrieve information for)
        """
        def set_ContactId(self, value):
            InputSet._set_input(self, 'ContactId', value)

        """
        Set the value of the Password input for this choreography. ((string) Your Constant Contact password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the UserName input for this choreography. ((string) Your Constant Contact username)
        """
        def set_UserName(self, value):
            InputSet._set_input(self, 'UserName', value)


"""
A ResultSet with methods tailored to the values returned by the ObtainContactInformation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ObtainContactInformationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Constant Contact)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ObtainContactInformationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ObtainContactInformationResultSet(response, path)
