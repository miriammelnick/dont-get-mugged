
###############################################################################
#
# CreateEntry
# Creates a new calendar entry in a specified project.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class CreateEntry(Choreography):

    """
    Create a new instance of the CreateEntry Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/37Signals/Basecamp/CreateEntry')


    def new_input_set(self):
        return CreateEntryInputSet()

    def _make_result_set(self, result, path):
        return CreateEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CreateEntryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the CreateEntry
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class CreateEntryInputSet(InputSet):
        """
        Set the value of the AccountName input for this choreography. ((required, string) A valid Basecamp account name. This is the first part of the account's URL.)
        """
        def set_AccountName(self, value):
            InputSet._set_input(self, 'AccountName', value)

        """
        Set the value of the EndDate input for this choreography. ((required, date) The date the entry ends, in YYYY-MM-DD format. This is the same as StartDate for one-day entries.)
        """
        def set_EndDate(self, value):
            InputSet._set_input(self, 'EndDate', value)

        """
        Set the value of the Password input for this choreography. ((required, string) The Basecamp account password. Use the value 'X' when specifying an API Key for the Username input.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the ProjectID input for this choreography. ((required, integer) The ID for the project in which to create the new entry.)
        """
        def set_ProjectID(self, value):
            InputSet._set_input(self, 'ProjectID', value)

        """
        Set the value of the ResponsibleParty input for this choreography. ((optional, any) The user ID or company ID (preceded by a “c”, as in "c1234") to assign the entry to. Applies only to "Milestone" entry types.)
        """
        def set_ResponsibleParty(self, value):
            InputSet._set_input(self, 'ResponsibleParty', value)

        """
        Set the value of the StartDate input for this choreography. ((required, date) The date the entry starts, in YYYY-MM-DD format.)
        """
        def set_StartDate(self, value):
            InputSet._set_input(self, 'StartDate', value)

        """
        Set the value of the Title input for this choreography. ((required, string) The title for the calendar entry to create.)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Type input for this choreography. ((required, string) The type of calendar entry to create, either "Milestone" or "CalendarEvent" (the default).)
        """
        def set_Type(self, value):
            InputSet._set_input(self, 'Type', value)

        """
        Set the value of the Username input for this choreography. ((required, string) A Basecamp account username or API Key.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the CreateEntry choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class CreateEntryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response returned from Basecamp.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class CreateEntryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return CreateEntryResultSet(response, path)
