
###############################################################################
#
# UpdateEntry
# Updates a calendar event or milestone in a project you specify. 
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class UpdateEntry(Choreography):

    """
    Create a new instance of the UpdateEntry Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/UpdateEntry')


    def new_input_set(self):
        return UpdateEntryInputSet()

    def _make_result_set(self, result, path):
        return UpdateEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return UpdateEntryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the UpdateEntry
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class UpdateEntryInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the EndDate input for this choreography. ((required, date) The new end date for the updated entry, in the format YYYY-MM-DD.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the EntryID input for this choreography. ((required, integer) The ID for the calendar entry to update.)
        """
        def set_EntryID(self, value):
            InputSet._set_input(self, 'EntryID', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ProjectID input for this choreography. ((required, integer) The ID of the project with the calendar entry to update.)
        """
        def set_ProjectID(self, value):
            InputSet._set_input(self, 'ProjectID', value)

        """
        Set the value of the ResponsibleParty input for this choreography. ((optional, any) The user ID or company ID (preceded by a “c”, as in "c1234") to reassign the entry to. Applies only to "Milestone" entry types.)
        """
        def set_ResponsibleParty(self, value):
            InputSet._set_input(self, 'ResponsibleParty', value)

        """
        Set the value of the StartDate input for this choreography. ((optional, date) The new start date for the updated entry, in the format YYYY-MM-DD.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the Title input for this choreography. ((optional, string) The new title for the updated entry.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Type input for this choreography. ((optional, string) The new type for the updated entry, either "CalendarEvent" (the default) or "Milestone".)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)

        """
        Set the value of the Username input for this choreography. ((required, string) A Basecamp account username or API Key.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the UpdateEntry choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class UpdateEntryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response returned from Basecamp.)
        """
        def get_Response(self):
            return self._output.get('Response', None)
        """
        Retrieve the value for the "TemplateOutput" output from this choreography execution. (The request created from the input template.)
        """
        def get_TemplateOutput(self):
            return self._output.get('TemplateOutput', None)

class UpdateEntryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return UpdateEntryResultSet(response, path)
