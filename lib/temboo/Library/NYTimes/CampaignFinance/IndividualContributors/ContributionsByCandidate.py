
###############################################################################
#
# ContributionsByCandidate
# Retrieve contributions made by individuals to a specific presidential candidate. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ContributionsByCandidate(Choreography):

    """
    Create a new instance of the ContributionsByCandidate Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/CampaignFinance/IndividualContributors/ContributionsByCandidate')


    def new_input_set(self):
        return ContributionsByCandidateInputSet()

    def _make_result_set(self, result, path):
        return ContributionsByCandidateResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ContributionsByCandidateChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ContributionsByCandidate
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ContributionsByCandidateInputSet(InputSet):
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
        Set the value of the CandidateFECID input for this choreography. ((required, string) Enter a cadidate's nine-digit FEC ID. IDs can be obtained by first running the CandidateSearch Choreo.)
        """
        def set_CandidateFECID(self, value):
            InputSet._set_input(self, 'CandidateFECID', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Enter json or xml.  Default is json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the ContributionsByCandidate choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ContributionsByCandidateResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ContributionsByCandidateChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ContributionsByCandidateResultSet(response, path)
