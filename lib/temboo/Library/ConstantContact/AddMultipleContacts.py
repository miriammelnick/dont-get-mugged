
###############################################################################
#
# AddMultipleContacts
# Creates multiple contacts in your Constant Contact list via the Activities bulk API.  The Choreo can use Excel or CSV files for the bulk upload.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class AddMultipleContacts(Choreography):

    """
    Create a new instance of the AddMultipleContacts Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/ConstantContact/AddMultipleContacts')


    def new_input_set(self):
        return AddMultipleContactsInputSet()

    def _make_result_set(self, result, path):
        return AddMultipleContactsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return AddMultipleContactsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the AddMultipleContacts
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class AddMultipleContactsInputSet(InputSet):
        """
        Set the value of the FileContents input for this choreography. ((conditional, multiline) The file contents of the list you want to upload. Should be in CSV format. Required unless using the VaultFile alias input (an advanced option used when running Choreos from the Temboo Designer).)
        """
        def set_FileContents(self, value):
            InputSet._set_input(self, 'FileContents', value)

        """
        Set the value of the APIKey input for this choreography. ((required, string) API Key provided by Constant Contact)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ListId input for this choreography. ((required, integer) The numberic id for the list that you want to add contacts to)
        """
        def set_ListId(self, value):
            InputSet._set_input(self, 'ListId', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Constant Contact password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the UserName input for this choreography. ((required, string) Your Constant Contact username)
        """
        def set_UserName(self, value):
            InputSet._set_input(self, 'UserName', value)

        """
        Set the value of the VaultFile input for this choreography. ((optional, vault file) A path to the vault CSV file you want to upload. Required unless using the FileContents input.)
        """


"""
A ResultSet with methods tailored to the values returned by the AddMultipleContacts choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class AddMultipleContactsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Constant Contact)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class AddMultipleContactsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return AddMultipleContactsResultSet(response, path)
