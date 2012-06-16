
###############################################################################
#
# ContributionsToPresidentialCandidates
# Retrieve contributions made by individuals to a specific presidential candidate. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ContributionsToPresidentialCandidates(Choreography):

    """
    Create a new instance of the ContributionsToPresidentialCandidates Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/CampaignFinance/IndividualContributors/ContributionsToPresidentialCandidates')


    def new_input_set(self):
        return ContributionsToPresidentialCandidatesInputSet()

    def _make_result_set(self, result, path):
        return ContributionsToPresidentialCandidatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ContributionsToPresidentialCandidatesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ContributionsToPresidentialCandidates
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ContributionsToPresidentialCandidatesInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CampaignCycle input for this choreography. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year.)
        """
        def set_CampaignCycle(self, value):
            InputSet._set_input(self, 'CampaignCycle', value)

        """
        Set the value of the CandidateFECID input for this choreography. ((conditional, string) Enter a candidate's nine-digit FEC ID. IDs can be obtained by first running the CandidateSearch Choreo. Required unless providing the LastName input.)
        """
        def set_CandidateFECID(self, value):
            InputSet._set_input(self, 'CandidateFECID', value)

        """
        Set the value of the LastName input for this choreography. ((conditional, string) Enter the name of a presidential candidate for whom contributions will be obtained. Required unless providing the CandidateFECID input.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Enter json or xml.  Default is json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the ContributionsToPresidentialCandidates choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ContributionsToPresidentialCandidatesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ContributionsToPresidentialCandidatesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ContributionsToPresidentialCandidatesResultSet(response, path)
