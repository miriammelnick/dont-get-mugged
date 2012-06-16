
###############################################################################
#
# BatchCSVInsert
# Create Salesforce Objects of any type (Account, Lead, Contact, etc) by specifying rows in CSV format.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class BatchCSVInsert(Choreography):

    """
    Create a new instance of the BatchCSVInsert Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Salesforce/BatchCSVInsert')


    def new_input_set(self):
        return BatchCSVInsertInputSet()

    def _make_result_set(self, result, path):
        return BatchCSVInsertResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return BatchCSVInsertChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the BatchCSVInsert
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class BatchCSVInsertInputSet(InputSet):
        """
        Set the value of the CSVInput input for this choreography. ((conditional, multiline) CSV data to insert. Column names must match Salesforce field names exactly. Required unless using the VaultFile alias (an advanced option used when running Choreos in the Temboo Designer).)
        """
        def set_CSVInput(self, value):
            InputSet._set_input(self, 'CSVInput', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Salesforce password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the SalesforceObjectType input for this choreography. ((optional, string) The object type that you are inserting (i.e.Lead, Contact, Account). Defaults to Lead.)
        """
        def set_SalesforceObjectType(self, value):
            InputSet._set_input(self, 'SalesforceObjectType', value)

        """
        Set the value of the SecurityToken input for this choreography. ((required, string) Your Salesforce security token for making API calls.)
        """
        def set_SecurityToken(self, value):
            InputSet._set_input(self, 'SecurityToken', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Salesforce username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the VaultCSVFile input for this choreography. (A path to a CSV file in the vault. Required unless specifying your data in CSVInput.)
        """


"""
A ResultSet with methods tailored to the values returned by the BatchCSVInsert choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class BatchCSVInsertResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Salesforce)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class BatchCSVInsertChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return BatchCSVInsertResultSet(response, path)
