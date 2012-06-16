
###############################################################################
#
# ConvertLead
# Converts a lead to a potential, account, or contact in your Zoho CRM account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ConvertLead(Choreography):

    """
    Create a new instance of the ConvertLead Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zoho/CRM/ConvertLead')


    def new_input_set(self):
        return ConvertLeadInputSet()

    def _make_result_set(self, result, path):
        return ConvertLeadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConvertLeadChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ConvertLead
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ConvertLeadInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Zoho)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Amount input for this choreography. ((required, decimal) Corresponds to the Amount field in Zoho)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the AssignTo input for this choreography. ((optional, string) Corresponds to the Assign To field in Zoho)
        """
        def set_AssignTo(self, value):
            InputSet._set_input(self, 'AssignTo', value)

        """
        Set the value of the ClosingDate input for this choreography. ((required, date) Corresponds to the Closing Date field in Zoho. Formatted like MM/dd/yyyy.)
        """
        def set_ClosingDate(self, value):
            InputSet._set_input(self, 'ClosingDate', value)

        """
        Set the value of the ContactRole input for this choreography. ((required, string) Corresponds to the Contact Role field in Zoho)
        """
        def set_ContactRole(self, value):
            InputSet._set_input(self, 'ContactRole', value)

        """
        Set the value of the CreatePotential input for this choreography. ((optional, boolean) Corresponds to the Create Potential field in Zoho. Defaults to 1 for true.)
        """
        def set_CreatePotential(self, value):
            InputSet._set_input(self, 'CreatePotential', value)

        """
        Set the value of the ID input for this choreography. ((required, integer) The ID for the lead that you wish to convert to a potential)
        """
        def set_ID(self, value):
            InputSet._set_input(self, 'ID', value)

        """
        Set the value of the LoginID input for this choreography. ((required, string) Your Zoho username (or login id))
        """
        def set_LoginID(self, value):
            InputSet._set_input(self, 'LoginID', value)

        """
        Set the value of the NotifyLeadOwner input for this choreography. ((optional, boolean) Corresponds to the Notify Lead Owner field in Zoho. Defaults to 0 for false.)
        """
        def set_NotifyLeadOwner(self, value):
            InputSet._set_input(self, 'NotifyLeadOwner', value)

        """
        Set the value of the NotifyNewEntityOwner input for this choreography. ((optional, boolean) Corresponds to the Notify New Entity Owner field in Zoho. Defaults to 0 for false.)
        """
        def set_NotifyNewEntityOwner(self, value):
            InputSet._set_input(self, 'NotifyNewEntityOwner', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zoho password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the PotentialName input for this choreography. ((required, string) Corresponds to the Potential Name field in Zoho)
        """
        def set_PotentialName(self, value):
            InputSet._set_input(self, 'PotentialName', value)

        """
        Set the value of the PotentialStage input for this choreography. ((required, string) Corresponds to the Potential Stage field in Zoho)
        """
        def set_PotentialStage(self, value):
            InputSet._set_input(self, 'PotentialStage', value)

        """
        Set the value of the Probability input for this choreography. ((required, integer) Corresponds to the Probability field in Zoho)
        """
        def set_Probability(self, value):
            InputSet._set_input(self, 'Probability', value)


"""
A ResultSet with methods tailored to the values returned by the ConvertLead choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ConvertLeadResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Zoho)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ConvertLeadChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ConvertLeadResultSet(response, path)
