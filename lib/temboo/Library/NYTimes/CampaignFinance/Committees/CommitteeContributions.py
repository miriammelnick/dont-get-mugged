
###############################################################################
#
# CommitteeContributions
# Obtain contributions made by a Political Action Committee (PAC) in an election cycle.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CommitteeContributions(Choreography):

    """
    Create a new instance of the CommitteeContributions Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/CampaignFinance/Committees/CommitteeContributions')


    def new_input_set(self):
        return CommitteeContributionsInputSet()

    def _make_result_set(self, result, path):
        return CommitteeContributionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CommitteeContributionsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CommitteeContributions
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CommitteeContributionsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CampaignCycle input for this choreography. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year. )
        """
        def set_CampaignCycle(self, value):
            InputSet._set_input(self, 'CampaignCycle', value)

        """
        Set the value of the CommitteeFECID input for this choreography. ((conditional, string) Enter a political action committee's FEC ID.  Either CommitteeFECID, OR Name must be provided.)
        """
        def set_CommitteeFECID(self, value):
            InputSet._set_input(self, 'CommitteeFECID', value)

        """
        Set the value of the Name input for this choreography. ((conditional, string) Enter the name of a political action committee (PAC) whose contributions will be obtained. Either Name or CommitteeFECID must be provided.)
        """
        def set_Name(self, value):
            InputSet._set_input(self, 'Name', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) The first 20 results are shown by default. To page through the results, set Offset to the appropriate value (e.g., Offset=40 displays results 41–60).)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Enter json or xml.  Default is json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the CommitteeContributions choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CommitteeContributionsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CommitteeContributionsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CommitteeContributionsResultSet(response, path)
