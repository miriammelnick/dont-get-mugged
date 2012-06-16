
###############################################################################
#
# CampaignContribution
# Retrieve detailed information on political campaign contributions, filtered by date, contributor, state, employer, campaign, etc.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CampaignContribution(Choreography):

    """
    Create a new instance of the CampaignContribution Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/InfluenceExplorer/CampaignContribution')


    def new_input_set(self):
        return CampaignContributionInputSet()

    def _make_result_set(self, result, path):
        return CampaignContributionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CampaignContributionChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CampaignContribution
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CampaignContributionInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API key provided by Sunlight Data Services.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Amount input for this choreography. ((optional, string) Enter the amount of dollars spent on lobbying.  Valid formats include: 500 (exactly $500); >|500 (greater than, or equal to 500); <|500 (less than or equal to 500).)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the ContributorName input for this choreography. ((optional, string) Specfiy the name of an individual, PAC, organization, or employer for which a full-text search will be performed.)
        """
        def set_ContributorName(self, value):
            InputSet._set_input(self, 'ContributorName', value)

        """
        Set the value of the ContributorsByState input for this choreography. ((optional, string) Enter a two-letter state designation from which the contribution is made.)
        """
        def set_ContributorsByState(self, value):
            InputSet._set_input(self, 'ContributorsByState', value)

        """
        Set the value of the Cycle input for this choreography. ((optional, string) Specify a yyyy-formatted election cycle. Example: 2012, or 2008|2012 to limit results between 2008 and 2012.)
        """
        def set_Cycle(self, value):
            InputSet._set_input(self, 'Cycle', value)

        """
        Set the value of the Date input for this choreography. ((optional, string) Specify a date of the contribution in ISO date format.  For example: 2006-08-06.  Or, ><|2006-08-06|2006-09-12 to limit results between specific dates.)
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the OrganizationName input for this choreography. ((optional, string) Specify a full-text search on employer, organization, and parent organization.)
        """
        def set_OrganizationName(self, value):
            InputSet._set_input(self, 'OrganizationName', value)

        """
        Set the value of the RecipientName input for this choreography. ((optional, string) Enter the full-text search on name of PAC or candidate receiving the contribution.)
        """
        def set_RecipientName(self, value):
            InputSet._set_input(self, 'RecipientName', value)

        """
        Set the value of the RecipientState input for this choreography. ((optional, string) Specify a two-letter state abbreviation for the state in which the recipient of contributions is running a campaign.)
        """
        def set_RecipientState(self, value):
            InputSet._set_input(self, 'RecipientState', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Indicates the desired format for the response. Accepted values are: json (the default), csv, and xls. Note when specifying xls, restults are returned as Base64 encoded data.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Seat input for this choreography. ((optional, string) Specify the type of political office being sought.  Examples: federal:senate (US Senate), federal:president (US President), state:governor.  For more info see documentation.)
        """
        def set_Seat(self, value):
            InputSet._set_input(self, 'Seat', value)

        """
        Set the value of the TransactionNamespace input for this choreography. ((optional, string) Filters on federal or state contributions. Valid namespaces are: urn:fec:transaction (for federal) or urn:nimsp:transaction (for state).)
        """
        def set_TransactionNamespace(self, value):
            InputSet._set_input(self, 'TransactionNamespace', value)


"""
A ResultSet with methods tailored to the values returned by the CampaignContribution choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CampaignContributionResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Influence Explorer. Corresponds to the ResponseFormat input. Defaults to json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CampaignContributionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CampaignContributionResultSet(response, path)
